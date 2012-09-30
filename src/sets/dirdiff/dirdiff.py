#!/usr/bin/env python2
# author: Ryan Flynn www.parseerror.com github.com/rflynn

"""
diff dir contents, recursively
reason about filenames and file contents
handles multiple files with the same content
"""

import os
import hashlib
from collections import defaultdict

def contents(path): return hashlib.sha1(open(path).read()).hexdigest()

def filesame(file1, file2): return contents(file1) == contents(file2)

def filelist(dir):
    s = set()
    for root, subdirs, files in os.walk(dir):
        s = s.union(set(root + '/' + f for f in files))
    return set(x.replace(dir + '/', '', 1) for x in s)

def mapcontents(dir,files):
    d = defaultdict(list)
    for f in files:
        d[contents(dir + '/' + f)].append(f)
    return d

def hashable(l): return set(map(tuple, l))

def dirdiff(dir1, dir2):
    before = filelist(dir1)
    after = filelist(dir2)
    unchanged = set(f for f in before.intersection(after)
                if filesame(dir1 + '/' + f, dir2 + '/' + f))
    beforecontents = mapcontents(dir1, before.difference(unchanged))
    aftercontents = mapcontents(dir2, after.difference(unchanged))
    renamed = dict((tuple(beforecontents[k]), aftercontents[k])
                for k in set(beforecontents.keys()).intersection(set(aftercontents.keys())))
    deleted = hashable(beforecontents.values()).difference(hashable(renamed.keys()))
    created = hashable(aftercontents.values()).difference(hashable(renamed.values()))
    return {'unchanged':unchanged, 'renamed':renamed, 'deleted':deleted, 'created':created}

if __name__ == '__main__':
    os.system('mkdir -p dir1; cd dir1; echo a>a.unchanged; echo b>b.deleted; echo c>c.renamed; echo c>c.renamed2')
    os.system('mkdir -p dir2/subdir; cd dir2; echo a>a.unchanged; echo c>c2.renamed; echo d>d.new; echo c>subdir/c3.multirenamed')
    expect = {
        'deleted': set([('b.deleted',)]),
        'renamed': {('c.renamed', 'c.renamed2'): ['subdir/c3.multirenamed', 'c2.renamed']},
        'unchanged' : set(['a.unchanged']),
        'created': set([('d.new',)])
    }
    result = dirdiff('dir1', 'dir2')
    print result
    assert result == expect


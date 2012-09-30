#!/usr/bin/env python2
# author: Ryan Flynn www.parseerror.com github.com/rflynn

"""
diff dir contents, recursively
reason about filenames and file contents
handles multiple files with the same content
"""

import os
import hashlib

def contents(path): return hashlib.sha1(open(path).read()).hexdigest()

def filesame(file1, file2): return contents(file1) == contents(file2)

def app(s,(root,_,files)): return [root+'/'+f for f in files] + s
def filesrecursive(dir): return set(x.replace(dir+'/', '', 1) for x in reduce(app, os.walk(dir), []))

def mapcontents(dir,files):
    d = dict()
    for f in files:
        d.setdefault(contents(dir+'/'+f), []).append(f)
    return d

def multiset(l): return set(map(tuple, l))

def dirdiff(dir1, dir2):
    before, after = filesrecursive(dir1), filesrecursive(dir2)
    unchanged = set(f for f in before & after if filesame(dir1+'/'+f, dir2+'/'+f))
    beforecontents = mapcontents(dir1, before - unchanged)
    aftercontents = mapcontents(dir2, after - unchanged)
    renamed = dict((tuple(beforecontents[k]), aftercontents[k])
                        for k in beforecontents.keys() if k in aftercontents)
    deleted = multiset(beforecontents.values()) - multiset(renamed.keys())
    created = multiset(aftercontents.values()) - multiset(renamed.values())
    return {'unchanged':unchanged, 'renamed':renamed, 'deleted':deleted, 'created':created}

if __name__ == '__main__':
    os.system('mkdir -p dir1; cd dir1; echo a>a.unchanged; echo b>b.deleted; echo c>c.renamed; echo c>c.renamed2')
    os.system('mkdir -p dir2/subdir; cd dir2; echo a>a.unchanged; echo c>c2.renamed; echo d>d.new; echo c>subdir/c3.multirenamed')
    expect = {
        'unchanged' : set(['a.unchanged']),
        'renamed': {('c.renamed', 'c.renamed2'): ['subdir/c3.multirenamed', 'c2.renamed']},
        'deleted': set([('b.deleted',)]),
        'created': set([('d.new',)])
    }
    result = dirdiff('dir1', 'dir2')
    print result
    assert result == expect

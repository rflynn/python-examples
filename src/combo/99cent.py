
target = 99
coins = [25,10,5,1] # U.S.

def exhaustive(sums, coins):
    need = dict([(c,0) for c in coins])
    for s in sums:
        for c in coins:
            cnt = int(s / float(c)) # how many of coin c fit in s?
            if cnt > need[c]: # remember this amt if it's more than we've used before
                need[c] = cnt
            s -= cnt * c
        assert s == 0 # combination of coins must exactly match s
    return need

print 'exhaustive:', exhaustive(range(1, target+1), coins)

def relative(coins):
    # but the relationship is actually much simpler than that:
    # it's based on the relative size of each coin to the next-highest coin
    maxc = [(c, int((nexthighest - 1) / float(c)))
        for nexthighest,c in zip(coins, coins[1:])]
    return dict(maxc)

rel = relative([target+1] + coins)
print 'relative:  ', rel

print 'the most coins needed to represent any sum will always be the amount needed to match the next-highest amount-1,'
print 'in this case we need %u coins to sum to %s' % (sum(rel.values()), target)


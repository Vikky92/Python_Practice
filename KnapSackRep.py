from itertools import combinations

#used to make 
def combine(items):
    ' return combinations of any length from the items '
    return ( combine 
             for r in range(1, len(items)+1)
             for combine in combinations(items, r)
             )

def TotalValue(combine):
    ' Totalise a particular combination of items'
    totalW = totalV = 0
    for item, wgt, val in combine:
        totalW  += wgt
        totalV += val
    return (totalV, -totalW) if totalW <= 11 else (0, 0)

#Using Memoization
def KnapSackDP(items, limit):
    array = [[0 for w in range(limit + 1)] for j in xrange(len(items) + 1)]
 
    for j in xrange(1, len(items) + 1):
        item, wgt, val = items[j-1]
        for w in xrange(1, limit + 1):
            if wgt > w:
                array[j][w] = array[j-1][w]
            else:
                array[j][w] = max(array[j-1][w],array[jt][w-wgt] + val) #DP function 
 
    result = []
    W = limit
    for j in range(len(items), 0, -1):
        was_added = (array[j][W] != array[j-1][W])  #appending the results table with the values only from last wgt = W column
 
        if was_added:
            item, wgt, val = items[j-1]
            result.append(items[j-1])
            W -= wgt
 
    return result
 
items = (
    ("apple",1,1),("banana",2,6),("carrot",5,18),("knife",6,22),("mover",7,28)
    )
 
chosen_in_bag = KnapSackDP(items,11)
print("The algorithm choses the following\n  " +
      '\n  '.join(sorted(item for item,_,_ in chosen_in_bag)))
val, wgt = TotalValue(chosen_in_bag)
print("for a total value of %i and a total weight of %i" % (val, -wgt))
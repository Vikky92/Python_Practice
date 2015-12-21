import bisect
import collections
class Interval(object):
    '''Date interval'''

    def __init__(self, weight, start, finish):
        self.weight = weight
        self.start = start
        self.finish = finish

    def __repr__(self):
        return str((self.weight, self.start, self.finish))

def schedule_unweighted_intervals(I):
    '''Use greedy algorithm to schedule unweighted intervals
       sorting is O(n log n), selecting is O(n)
       whole operation is dominated by O(n log n)
    '''

    I.sort(lambda x, y: x.finish - y.finish)  # f_1 <= f_2 <= .. <= f_n

    O = []
    finish = 0
    for i in I:
        if finish <= i.start:
            finish = i.finish
            O.append(i)

    return O

def calculate_previous_intervals(I):
    '''For every interval j, calculate\
     the rightmost mutually compatible interval i, where i < j
       I is a sorted list of Interval objects (sorted by finish time)
    '''
    # extract start and finish times
    start = [i.start for i in I]
    finish = [i.finish for i in I]

    p = []
    for j in xrange(len(I)):
        i = bisect.bisect_right(finish, start[j]) - 1  # rightmost interval f_i <= s_j
        p.append(i)

    return p
    
i1=Interval(2,1,5)
i2=Interval(4,1,9)
i3=Interval(4,5,10)
i4=Interval(7,6,9)
i5=Interval(2,10,12)

I= [i1,i2,i3,i4,i5]
I= schedule_unweighted_intervals(I)

i=0
for i in I: 
	print i

I1= [i1,i2,i3,i4,i5]
p=calculate_previous_intervals(I1)

for i in p: 
	print i

OPT = collections.defaultdict(int)
OPT[-1] = 0
OPT[0] = 0
for j in xrange(1, len(I)):
    OPT[j] = max(I1[j].weight + OPT[p[j]], OPT[j - 1])

'''Memoization'''
O = []
def compute_solution(j):
    if j >= 0:  # will halt on OPT[-1]
        if I1[j].weight + OPT[p[j]] > OPT[j - 1]:
            O.append(I1[j])
            compute_solution(p[j])
        else:
            compute_solution(j - 1)
compute_solution(len(I1) - 1)

''' This is using Iterative '''
OPT = collections.defaultdict(int)
OPT[-1] = 0
OPT[0] = 0
for j in xrange(1, len(I)):
    OPT[j] = max(I1[j].weight + OPT[p[j]], OPT[j - 1])

for i in O:
	print i 







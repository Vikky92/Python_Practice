
def KnapSack(weights, values, W):

    # initialize K
    # K(w) = maximum value for capacity w
    K = [0]*(W+1)

    # start from w=0 to w=W
    for j in range(0, len(weights)):
    	
    	for w in range(0, W+1):
        # temporary store the values after adding item j to K[w-weights[j]]
        #val = []
        # loop through each item to determine which one to add
        #for j in range(0, len(weights)):
            # make sure the item is less than w to prevent overloading the capacity
            if weights[j] <= w:
            	K[w] = max(K[w], values[j] + K[w-weights[j]])
                #val.append(K[w-weights[j]] + values[j])
        print K[w]
        # choose the item that results in the maximum value
        	#K[w] = max(K[w], K[w-weights[j]])
        	
    
    
    print 'The maximum value of the knapsack is ', int(K[W])
 

    
'num = raw_input("Enter how many items you want:")'
'''for i in range(int(num)):
    n = raw_input("weight")
    weights.append(int(n))
print 'Weights ',weights
'''
weights1=[6,3,4,2]
values1=[30,14,16,9]

W1=10

weights2=[580,1616,1906,1942,50,294]
values2=[874,620,345,369,360,470]

W2=2000
'''for i in range(int(num)):
    n = raw_input("Values")
    values.append(int(n))
print 'values ',values
'''    
print KnapSack(weights1,values1,W1)
print KnapSack(weights2,values2,W2)

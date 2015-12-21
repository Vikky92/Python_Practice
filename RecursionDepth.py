def trav(seq, i=0):
	if i==len(seq): 
		return trav(seq, i+1)
		
trav(range(1000))
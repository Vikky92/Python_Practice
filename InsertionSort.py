def ins_sort(seq):
	for i in range(1,len(seq)):
		j=i
		while j > 0 and seq[j-1] > seq[j]:
			seq[j-1], seq[j] = seq[j], seq[j-1] 
			j -= 1
			
seq=[4,1,2,6,7,2,10,11,0]
ins_sort(seq)
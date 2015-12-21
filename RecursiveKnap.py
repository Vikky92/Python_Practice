
# each item to be packed is represented as a set of triples (size,value,name)
def itemSize(item): return item[0]
def itemValue(item): return item[1]
def itemName(item): return item[2]

exampleItems = [(3,3,'A'),
		(4,1,'B'),
		(8,3,'C'),
		(10,4,'D'),
		(15,3,'E'),
		(20,6,'F')]
		
exampleSizeLimit = 32

# inefficient recursive algorithm
# returns optimal value for given
#
# note items[-1] is the last item, items[:-1] is all but the last item
#
def pack1(items,sizeLimit):
	if len(items) == 0:
		return 0
	elif itemSize(items[-1]) > sizeLimit:
		return pack(items[:-1],sizeLimit)
	else:
		return max(pack(items[:-1],sizeLimit) ,pack(items[:-1],sizeLimit-itemSize(items[-1])) + itemValue(items[-1]))

def pack2(items,sizeLimit):
	def recurse(nItems,lim):
		if nItems == 0:
			return 0
		elif itemSize(items[nItems-1]) > lim:
			return recurse(nItems-1,lim)
		else:
			return max(recurse(nItems-1,lim),
				   recurse(nItems-1,lim-itemSize(items[nItems-1])) +
					itemValue(items[nItems-1]))
	return recurse(len(items),sizeLimit)

print pack2(exampleItems,exampleSizeLimit)
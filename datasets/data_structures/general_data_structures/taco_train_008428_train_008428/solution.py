def heapify(i):
	p = (i - 1) // 2
	while p >= 0:
		if heap[p] > heap[i]:
			(heap[p], heap[i]) = (heap[i], heap[p])
		i = p
		p = (p - 1) // 2

def insertKey(x):
	global curr_size
	heap[curr_size] = x
	heapify(curr_size)
	curr_size = curr_size + 1

def heapify2(i):
	global curr_size
	l = i * 2 + 1
	r = i * 2 + 2
	k = i
	if l < curr_size and heap[l] < heap[i]:
		i = l
	if r < curr_size and heap[r] < heap[i]:
		i = r
	if i != k:
		(heap[i], heap[k]) = (heap[k], heap[i])
		heapify2(i)

def deleteKey(i):
	global curr_size
	if i >= curr_size:
		return -1
	heap[i] = float('-inf')
	heapify(i)
	heap[0] = heap[curr_size - 1]
	heap[curr_size - 1] = 0
	curr_size = curr_size - 1
	heapify2(0)

def extractMin():
	global curr_size
	if curr_size == 0:
		return -1
	pos = heap[0]
	heap[0] = heap[curr_size - 1]
	heap[curr_size - 1] = 0
	curr_size = curr_size - 1
	heapify2(0)
	return pos

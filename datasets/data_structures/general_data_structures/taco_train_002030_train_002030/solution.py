class Node:

	def __init__(self, key):
		self.key = key
		self.high = 0
		self.data = 0
		self.nexts = []
		self.previous = None

def update(head, V, K, d):
	if head is None:
		return
	head.data += V + d * K
	for n in head.nexts:
		update(n, V, K, d + 1)

def report(start, end, root):
	if start is None or end is None:
		return
	limit = pow(10, 9) + 7
	higherNode = start
	lowerNode = end
	if start.high < end.high:
		higherNode = end
		lowerNode = start
	distance = higherNode.high - lowerNode.high
	_sum = 0
	while higherNode.high > lowerNode.high:
		_sum += higherNode.data
		if _sum > limit:
			_sum %= limit
		higherNode = higherNode.previous
	while higherNode.data != lowerNode.data:
		_sum += higherNode.data
		_sum += lowerNode.data
		if _sum > limit:
			_sum %= limit
		higherNode = higherNode.previous
		lowerNode = lowerNode.previous
	_sum += higherNode.data
	if _sum > limit:
		_sum %= limit
	print(_sum)

def correctVector(head, high):
	if head is None:
		return
	for node in head.nexts:
		node.previous = head
		node.nexts.remove(head)
		node.high = high
		correctVector(node, high + 1)

def resolve(data):
	configs = data[0].split(' ')
	N = int(configs[0])
	E = int(configs[1])
	root = configs[2]
	nodes = {}
	for i in range(1, N):
		items = data[i].split(' ')
		first = items[0]
		second = items[1]
		if first in nodes:
			firstNode = nodes[first]
		else:
			firstNode = Node(first)
			nodes[first] = firstNode
		if second in nodes:
			secondNode = nodes[second]
		else:
			secondNode = Node(second)
			nodes[second] = secondNode
		firstNode.nexts.append(secondNode)
		secondNode.nexts.append(firstNode)
	correctVector(nodes[root], 1)
	for i in range(N, N + E):
		items = data[i].split(' ')
		itemType = items[0]
		if itemType == 'U':
			update(nodes[items[1]], int(items[2]), int(items[3]), 0)
		elif itemType == 'Q':
			report(nodes[items[1]], nodes[items[2]], nodes[root])
import sys
data = [s.strip() for s in sys.stdin]
resolve(data)

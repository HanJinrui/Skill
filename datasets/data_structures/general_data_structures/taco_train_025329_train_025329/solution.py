def push(x):
	global queue_1
	global queue_2
	queue_1.append(x)

def pop():
	global queue_1
	global queue_2
	return queue_1.pop() if queue_1 else -1

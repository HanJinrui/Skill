def modifyQueue(q, k):
	return q[:k][::-1] + q[k:]

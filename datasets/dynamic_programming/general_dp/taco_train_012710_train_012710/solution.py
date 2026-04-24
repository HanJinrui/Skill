from sys import stdin, stdout
max_k = 10000
max_shift = [max_k]
for t in range(1, 5):
	max_shift.append(max_shift[t - 1] * (max_k + 1) + max_k)

def get_right(left, t):
	if left >= max_k:
		return left + max_shift[t - 1] - 1
	k = left
	if k > max_k:
		k = max_k
	if t == 1:
		return left + k - 1
	new_left = left
	for i in range(k):
		new_left = get_right(new_left, t - 1) + 2
	return get_right(new_left, t - 1)
left = 1
right = 10004205361450474
k = 1
for t in range(5, 0, -1):
	if t == 1:
		right = get_right(left, 1)
		request = range(left, right + 1)
	else:
		request = []
		request_item = left - 1
		for i in range(k):
			request_item = get_right(request_item + 1, t - 1) + 1
			request.append(request_item)
	print(len(request), ' '.join([str(x) for x in request]))
	stdout.flush()
	reply = int(stdin.readline())
	if reply in (-1, -2):
		exit()
	if reply > 0:
		left = request[reply - 1] + 1
	k = left
	if k > max_k:
		k = max_k

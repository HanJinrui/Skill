n = int(input())
a = [0] * n
b = [0] * n
c = [0] * n
for i in range(n):
	(a[i], b[i], c[i]) = map(int, input().split())
middle = {}
stack = []
result = (-10000000000.0, ())
phase = 1

def search(pos, l, m, w):
	global result
	if pos == n >> 1 if phase == 1 else pos < n >> 1:
		if phase == 1:
			middle[m - l, w - l] = (stack[:], l)
		else:
			(seq, first_l) = middle.get((l - m, l - w), (None, None))
			if seq is not None and l + first_l > result[0]:
				result = (l + first_l, seq + stack[::-1])
	else:
		stack.append('LM')
		search(pos + phase, l + a[pos], m + b[pos], w)
		stack[-1] = 'LW'
		search(pos + phase, l + a[pos], m, w + c[pos])
		stack[-1] = 'MW'
		search(pos + phase, l, m + b[pos], w + c[pos])
		stack.pop()
search(0, 0, 0, 0)
phase = -1
search(n - 1, 0, 0, 0)
if result[1]:
	print('\n'.join(result[1]))
else:
	print('Impossible')

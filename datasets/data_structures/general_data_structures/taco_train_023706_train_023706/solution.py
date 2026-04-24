n = int(input())
num = sorted([(int(x), i + 1) for (i, x) in enumerate(input().split())])
m = n + 1

def Sum(s, n):
	ret = s[0]
	while n > 0:
		ret += s[n]
		n = n ^ n & ~n + 1
	return ret

def Update(s, n, v):
	while n <= m:
		s[n] += v
		n += n & ~n + 1
s = [[0] * (m + 1), [0] * (m + 1), [0] * (m + 1), [0] * (m + 1)]
s[0][0] = 1
for (i, (n, id)) in enumerate(num):
	if i and num[i - 1][0] == num[i][0]:
		continue
	process = [(n, id)]
	if i + 1 < len(num) and num[i][0] == num[i + 1][0]:
		process.append(num[i + 1])
	for state in (3, 2, 1):
		values = []
		for (n, id) in process:
			values.append(Sum(s[state - 1], id - 1))
		if len(values) > 1:
			values[1] -= values[0]
		for (j, (n, id)) in enumerate(process):
			Update(s[state], id, values[j])
print(Sum(s[3], m - 1))

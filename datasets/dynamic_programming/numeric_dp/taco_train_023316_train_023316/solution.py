def solve0(x):
	lr = (max(x) + 1) * len(x) + 1
	ret = [0] * lr
	ret[0] = 1
	for y in x:
		ret0 = [0] * lr
		for (i, z) in enumerate(ret):
			if z == 0:
				continue
			for j in range(i, i + y + 1):
				ret0[j] += z
		ret = ret0
	q = 0
	for i in range(100):
		j = 1 << i
		if j >= len(ret):
			break
		q += ret[j]
	return q

def solve(x):
	ret = 0
	for i in range(1, max(x) + 1):
		if i % 2 == 1:
			y = [z // i for z in x]
			ret += solve0(y)
	return ret
import sys
f = sys.stdin
t = int(f.readline())
x = list(map(int, f.readline().split()))
print(solve(x) % (10 ** 9 + 7))

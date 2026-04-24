input()
y = list(map(int, input().split()))

def check(d):
	return len(set((j - d * i for (i, j) in enumerate(y)))) == 2
d = ((y[2] - y[0]) / 2, y[1] - y[0], y[2] - y[1])
print('yes' if any((check(dx) for dx in d)) else 'no')

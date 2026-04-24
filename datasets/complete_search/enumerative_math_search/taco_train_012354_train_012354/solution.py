co = lambda z: bin(z).count('1')

def bruteforce(n, a):
	for i in range(n):
		for j in range(n):
			for k in range(n):
				for l in range(n):
					net = set([i, j, k, l])
					if len(net) == 4:
						x = a[i] ^ a[j]
						y = a[k] ^ a[l]
						if co(x) == co(y):
							print(i + 1, j + 1, k + 1, l + 1)
							return
	print(-1)
	return

def solve(n, a):
	net = [-1] * 32
	for i in range(0, n - 1, 2):
		k = co(a[i] ^ a[i + 1])
		if net[k] != -1:
			print(i + 1, i + 2, net[k] + 1, net[k] + 2)
			return
		net[k] = i
for _ in range(int(input())):
	n = int(input())
	a = tuple(map(int, input().split()))
	if n <= 62:
		bruteforce(n, a)
	else:
		solve(n, a)

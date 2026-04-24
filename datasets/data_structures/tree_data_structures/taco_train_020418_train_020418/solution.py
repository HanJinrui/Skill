from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(10 ** 6)

def dfs(p, prev):
	count = 0
	for i in child[p]:
		if i == prev:
			continue
		count += dfs(i, p)
	return count + (a[p - 1] == 'B')

def answer():
	for i in range(1, n + 1):
		count = dfs(i, -1)
		if count > 1:
			return 'No'
	return 'Yes'
for T in range(int(input())):
	n = int(input())
	a = input().strip()
	child = [[] for i in range(n + 1)]
	for i in range(n - 1):
		(u, v) = map(int, input().split())
		if a[u - 1] == 'R' and a[v - 1] == 'G':
			continue
		if a[u - 1] == 'G' and a[v - 1] == 'R':
			continue
		child[u].append(v)
		child[v].append(u)
	print(answer())

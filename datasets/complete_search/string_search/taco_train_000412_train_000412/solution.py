import sys
input = sys.stdin.readline
for t in range(int(input())):
	n = int(input())
	s = input()
	k = input().split()[1:]
	m = e = 0
	for i in range(n):
		if s[i] in k:
			e = max(e, i - m)
			m = i
	print(e)

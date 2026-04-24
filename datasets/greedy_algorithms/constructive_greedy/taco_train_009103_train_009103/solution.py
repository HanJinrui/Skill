input()
t = list(map(int, input().split()))
s = sorted(t)
for q in t:
	print(s[s.index(q) - 1])

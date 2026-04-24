a = int(input())
n = list(map(int, input().split()))
m = n[:1]
for i in n:
	a -= min(m) <= i <= max(m)
	m += [i]
print(a)

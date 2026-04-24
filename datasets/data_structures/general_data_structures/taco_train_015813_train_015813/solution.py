n = int(input())
d = {}
for i in range(n):
	s = input().split()
	d[s[0]] = sum(map(float, s[1:])) / 3
print('{:.2f}'.format(d[input()]))

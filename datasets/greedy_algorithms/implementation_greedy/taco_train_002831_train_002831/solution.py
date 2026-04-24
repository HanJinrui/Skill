input()
s = list(map(int, input().split()))
k = 0
while s[0] <= max(s[1:]):
	s[1 + s[1:].index(max(s))] -= 1
	s[0] += 1
	k += 1
print(k)

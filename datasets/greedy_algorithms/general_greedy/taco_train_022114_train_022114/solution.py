input()
s = 0
for i in reversed(list(map(int, input().split()))):
	s += i
	s = (s + s % 2) // 2
print(s)

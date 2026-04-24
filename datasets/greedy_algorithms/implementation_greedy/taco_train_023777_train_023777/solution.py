n = int(input())
s = set()
for x in map(int, input().split()):
	while x in s:
		s.remove(x)
		x += 1
	s.add(x)
print(max(s) - len(s) + 1)

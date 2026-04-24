n = int(input())
l1 = [input() for _ in range(n)]
for i in range(n):
	s = input()
	if s in l1:
		l1.remove(s)
print(len(l1))

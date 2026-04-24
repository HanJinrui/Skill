input()
f = 0
for a in map(int, input().split()):
	if f > a:
		break
	f ^= a & 1
print(('YES', 'NO')[f])

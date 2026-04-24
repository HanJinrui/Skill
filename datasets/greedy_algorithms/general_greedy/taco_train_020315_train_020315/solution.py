input()
B = []
b = neg = 0
for a in map(int, input().split()):
	if a < 0:
		if neg > 1:
			B.append(b)
			b = neg = 0
		neg += 1
	b += 1
print(len(B) + 1)
print(*B, b)

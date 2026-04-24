n = int(input())

strengths = []

for troop in range(n):
	strengths.append(int(input()))


sum = sum(strengths)

if n <= 3:
	print(max(strengths))

else:
	print((sum / 3) + 1)

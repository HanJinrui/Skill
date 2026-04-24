input()
a = input().split()
l = [0] * 212345
for i in a:
	for j in a:
		l[int(i) + int(j)] += 1 * (i != j)
print(max(l) // 2)

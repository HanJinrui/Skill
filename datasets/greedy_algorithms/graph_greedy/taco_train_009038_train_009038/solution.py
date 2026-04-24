a = int(input())
input()
z = [pow(10, 9)] * a
for i in range(int(input())):
	(a, b) = map(int, input().split()[1:])
	z[a - 1] = min(z[a - 1], b)
z.remove(max(z))
if pow(10, 9) in z:
	print(-1)
else:
	print(sum(z))

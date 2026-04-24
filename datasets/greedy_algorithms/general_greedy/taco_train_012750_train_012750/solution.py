n = int(input())
l = sorted([int(x) for x in input().split()], reverse=True)
for x in range(n - 2):
	temp = l[x:x + 3]
	if temp[0] < temp[1] + temp[2]:
		print(*reversed(temp))
		break
else:
	print(-1)

n = int(input())
s = set(map(int, input().split()))
m = max(s)
ans = [m]
for x in s:
	i = 1
	while x + i <= m:
		y = x + i
		if y in s:
			ans = [x, y]
			if y + i in s:
				print(3)
				print(x, y, y + i)
				exit()
		i *= 2
print(len(ans))
print(*ans)

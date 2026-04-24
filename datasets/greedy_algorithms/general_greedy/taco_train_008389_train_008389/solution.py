from collections import Counter
n = int(input())
l = list(map(int, input().split()))
ans = [0] * (max(l) + 1)
for i in l:
	ans[i] += 1
mn = ans[1]
for x in range(1, len(ans)):
	if ans[x] > mn:
		print(-1)
		exit()
	else:
		mn = ans[x]
print(ans[1])
for y in l:
	print(ans[y], end=' ')
	ans[y] -= 1

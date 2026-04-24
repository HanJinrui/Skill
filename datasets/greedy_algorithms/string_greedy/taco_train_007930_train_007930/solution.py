(n, t) = map(int, input().split())
s1 = input()
s2 = input()
ans = ['' for i in range(n)]
k = n - t
for i in range(n):
	if k == 0:
		break
	if s1[i] == s2[i]:
		ans[i] = s1[i]
		k -= 1
k1 = k
k2 = k
for i in range(n):
	if ans[i] != '':
		continue
	if 0 != k1 >= k2:
		ans[i] = s1[i]
		k1 -= 1
	elif 0 != k2 >= k1:
		ans[i] = s2[i]
		k2 -= 1
	elif k1 == k2 == 0:
		if s1[i] != 'a' != s2[i]:
			ans[i] = 'a'
		elif s1[i] != 'b' != s2[i]:
			ans[i] = 'b'
		else:
			ans[i] = 'c'
if k1 > 0 or k2 > 0:
	print(-1)
else:
	print(*ans, sep='')

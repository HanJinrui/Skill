def good(n):
	while n > 0:
		if n % 10 != 4 and n % 10 != 7:
			return False
		n //= 10
	return True
n = int(input())
a = list(map(int, input().split()))
b = [i for i in range(n)]
b.sort(key=lambda i: a[i])
g = -1
for i in range(n):
	if good(a[i]):
		g = i
		break
ans = []
ok = True
if g != -1:
	for i in range(n):
		a[b[i]] = i
	for i in range(n):
		if b[i] == i or b[i] == g:
			continue
		if i != g:
			ans.append('{} {}'.format(i + 1, g + 1))
			(b[a[i]], b[a[g]]) = (b[a[g]], b[a[i]])
			(a[i], a[g]) = (a[g], a[i])
		g = b[i]
		if i != g:
			ans.append('{} {}'.format(i + 1, g + 1))
			(b[a[i]], b[a[g]]) = (b[a[g]], b[a[i]])
			(a[i], a[g]) = (a[g], a[i])
else:
	for i in range(1, n):
		if a[i] < a[i - 1]:
			ok = False
			break
if not ok:
	print(-1)
else:
	print(len(ans))
	print('\n'.join(ans))

n = int(input())
a = list(map(int, input().split()))
ans = ''
l = 0
r = n - 1
last = -1
while l <= r:
	if min(a[l], a[r]) <= last:
		break
	if a[l] < a[r]:
		ans += 'L'
		last = a[l]
		l += 1
	elif a[l] > a[r]:
		ans += 'R'
		last = a[r]
		r -= 1
	else:
		break
last1 = last
ans1 = ans
l1 = l
while l1 <= r and a[l1] > last1:
	ans1 += 'L'
	last1 = a[l1]
	l1 += 1
last2 = last
ans2 = ans
r2 = r
while r2 >= l and a[r2] > last2:
	ans2 = ans2 + 'R'
	last2 = a[r2]
	r2 -= 1
if len(ans1) > len(ans2):
	print(len(ans1))
	print(ans1)
else:
	print(len(ans2))
	print(ans2)

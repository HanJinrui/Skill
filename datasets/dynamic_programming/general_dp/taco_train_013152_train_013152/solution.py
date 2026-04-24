from random import choice
n = int(input())
a = list(map(int, input().split()))
ans = []
if len(a) == 1:
	print(1)
	exit()
if a[0] == a[1]:
	c = 0
	ans += [2, 3]
elif a[0] > a[1]:
	c = -1
	ans += [5, 4]
	t = 4
else:
	c = 1
	ans += [1, 2]
	t = 2
for i in range(2, n):
	if a[i] > a[i - 1]:
		if c != 1:
			if ans[-2] == 1:
				t = 2
			else:
				t = 1
			ans[-1] = t
		t += 1
		c = 1
		ans.append(t)
	elif a[i] == a[i - 1]:
		c = 0
		ans.append(choice(list({2, 3, 4} - {ans[-1]})))
	elif a[i] < a[i - 1]:
		if c != -1:
			if ans[-2] == 5:
				t = 4
			else:
				t = 5
			ans[-1] = t
		t -= 1
		c = -1
		ans.append(t)
	if ans[-1] > 5 or ans[-1] < 1:
		ans = [-1]
		break
print(*ans)

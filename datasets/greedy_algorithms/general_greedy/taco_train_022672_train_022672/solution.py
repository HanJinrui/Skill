(n, b, a) = map(int, input().split())
(s, m) = (input().split(), a)
for i in range(n):
	if b == 0 and m == 0:
		print(i)
		break
	if s[i] == '1' and b > 0 and (m < a):
		m += 1
		b -= 1
	elif m:
		m -= 1
	else:
		b -= 1
else:
	print(n)

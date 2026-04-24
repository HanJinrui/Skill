(n, p, q) = map(int, input().split())
X = []
while n > 0:
	if n % p:
		n -= q
		X.append(q)
	else:
		X += [p] * (n // p)
		break
if n < 0:
	print(-1)
else:
	print(len(X))
	(s, i) = (input(), 0)
	for x in X:
		print(s[i:i + x])
		i += x

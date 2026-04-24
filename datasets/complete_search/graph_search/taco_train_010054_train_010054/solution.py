(a, b) = map(int, input().split())
r = [b]
while b > a:
	d = b % 10
	if d == 1:
		b //= 10
	elif d % 2:
		break
	else:
		b //= 2
	r += [b]
r = r[::-1]
print([f"YES\n{len(r)}\n{' '.join(map(str, r))}", 'NO'][a != b])

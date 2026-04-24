def print_set(n):
	print(len(n))
	n = [str(i) for i in n]
	print(' '.join(n))
(a, b) = map(int, input().split())
s = a + b
used = 0
k = 1
A = []
B = []
while used + k <= s:
	used += k
	k += 1
k -= 1
while k > 0:
	if k <= a:
		A.append(k)
		a -= k
	else:
		b -= k
		B.append(k)
	k -= 1
print_set(A)
print_set(B)

t = input().split()
n = int(t[0])
d = float(t[1])
(r, k) = (0, 0)
while r < d:
	k += 1
	r = 1 - ((n - k) * (n - k - 1) * (n - k - 2) / 6 + 0.5 * k * (n - k) * (n - k - 1) / 2) / (n * (n - 1) * (n - 2) / 6)
print(k)

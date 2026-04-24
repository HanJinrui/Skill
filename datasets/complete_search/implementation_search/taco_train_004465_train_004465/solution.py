from sys import stdin

def read():
	return map(int, stdin.readline().split())

def ways(h, w, area):
	if area == h * w:
		return 2 * ((h + 1) // 2 * (w + 1) // 2) - 1
	if area > h * w:
		return 0
	if area < h + w - 1:
		return 0
	area = h * w - area
	if area % 4 != 0:
		return 0
	area //= 4
	ans = 0
	h //= 2
	w //= 2
	for a in range(1, h + 1):
		if area % a == 0 and area // a <= w:
			ans += 1
	return ans * 2
(n, m, s) = read()
ans = 0
for h in range(1, n + 1, 2):
	for w in range(1, m + 1, 2):
		ans += ways(h, w, s) * (n - h + 1) * (m - w + 1)
print(ans)

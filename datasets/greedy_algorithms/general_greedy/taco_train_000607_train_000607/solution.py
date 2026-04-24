from sys import stdin

def main():
	nextint = iter(map(int, stdin.read().split())).__next__
	n, k, d = nextint(), nextint(), nextint()
	arr = [nextint() for _ in range(n)]
	csum = sum(arr[:k - 1])
	for x in range(k - 1, n):
		csum += arr[x]
		if csum == 0:
			print(-1)
			return
		csum -= arr[x - (k - 1)]
	count, lastnz, pick = 0, -1, [0]*n
	csum = 0
	x = 0
	while x < n:
		if arr[x]:
			lastnz = x
		csum += arr[x]
		pick[x] = 1
		if x < k - 1:
			x += 1
			continue
		if pick[x - k]:
			csum -= arr[x - k]
		if csum < d:
			count += 1
			csum = 0
			pick[x] = 0
			x = lastnz + 2*k - 1
			for y in range(lastnz + k, min(lastnz + 2*k - 1, n)):
				if arr[y]:
					lastnz = y
				pick[y] = 1
				csum += arr[y]
		else:
			x += 1
	print(count)

main()

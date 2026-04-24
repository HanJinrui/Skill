def main():
	from sys import stdin
	input()
	read = stdin.readline
	for x in stdin:
		(N, K) = map(int, x.split())
		if K:
			B = [int(i) for i in read().split()]
			B.append(N + 1)
			B.sort()
			ans = B[0] * (B[0] - 1) // 2
			for i in range(1, K + 1):
				if B[i - 1] > ans:
					break
				ans += (B[i] * (B[i] - 1) - B[i - 1] * (B[i - 1] + 1)) // 2
		else:
			ans = N * (N + 1) // 2
		print('Mom' if ans % 2 else 'Chef')
main()

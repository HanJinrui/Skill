def candles_counting(N, K, A):

	def read(T, i):
		s = 0
		while i > 0:
			s += T[i]
			s %= 1000000007
			i -= i & -i
		return s

	def update(T, i, v):
		while i <= 50010:
			T[i] += v
			T[i] %= 1000000007
			i += i & -i
		return v

	def count_bits(b):
		c = 0
		while b:
			b &= b - 1
			c += 1
		return c
	L = 2 ** K
	R = 0
	for i in range(L):
		T = [0 for _ in range(50010)]
		t = 0
		for j in range(N):
			(h, c) = A[j]
			if i >> c - 1 & 1:
				t += update(T, h, read(T, h - 1) + 1)
				t %= 1000000007
		if count_bits(i) % 2 == K % 2:
			R += t
			R %= 1000000007
		else:
			R += 1000000007 - t
			R %= 1000000007
	return R

def main():
	(N, K) = [int(i) for i in input().split()]
	A = []
	for _ in range(N):
		A.append([int(i) for i in input().split()])
	print(candles_counting(N, K, A))
main()

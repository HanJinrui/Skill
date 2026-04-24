(N, K) = map(int, input().split())
S = input().strip()
A = [ord(c) - 65 for c in S]
h = 1
while h <= K:
	if h & K:
		A = [A[i] ^ A[(i + h) % N] for i in range(N)]
	h <<= 1
S = ''.join((chr(c + 65) for c in A))
print(S)

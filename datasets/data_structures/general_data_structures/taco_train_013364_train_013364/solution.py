def Function(S):
	result = 0
	for (i, s) in enumerate(reversed(S)):
		result += ord(s) * (10 ** 5 + 1) ** i
		result %= 10 ** 9 + 7
	return result

def FindPalindromes(S, left, right):
	result = []
	while left >= 0 and right < len(S) and (S[left] == S[right]):
		result += [S[left:right + 1]]
		left -= 1
		right += 1
	return result
(_, nQueries) = map(int, input().split())
S = input()
result = list(S)
for i in range(len(S)):
	result += FindPalindromes(S, i - 1, i)
	result += FindPalindromes(S, i - 1, i + 1)
result.sort()
for __ in range(nQueries):
	K = int(input()) - 1
	print(Function(result[K]) if K < len(result) else -1)

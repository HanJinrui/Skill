n = int(input())
S = input()
k = ''
i = 0
while i < n - 1:
	if S[i] != S[i + 1]:
		k += S[i] + S[i + 1]
		i += 2
		continue
	i += 1
print(n - len(k))
print(k)

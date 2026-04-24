(a, b) = input().split('|')
S = a + input() + b
s = len(S) // 2
print([S[:s] + '|' + S[s:], 'Impossible'][max(map(len, [a, b, S[s:]])) > s])

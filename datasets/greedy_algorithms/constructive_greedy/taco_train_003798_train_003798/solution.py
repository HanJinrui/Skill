(n, k) = map(int, input().split())
v = ['AB'[i // 26] + 'abcdefghijklmnopqrstuvwxyz'[i % 26] for i in range(n)]
for (i, si) in enumerate(input().split()):
	if si == 'NO':
		v[i + k - 1] = v[i]
print(' '.join(v))

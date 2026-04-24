(b, p) = map(int, input().split())
s1 = input()
s2 = input()
cnt = [0] * len(s2)
nxt = [0] * len(s2)
for i in range(len(s2)):
	pos = i
	for j in range(len(s1)):
		if s1[j] == s2[pos]:
			pos += 1
			if pos == len(s2):
				cnt[i] += 1
				pos = 0
	nxt[i] = pos
ans = 0
poss = 0
for i in range(b):
	ans += cnt[poss]
	poss = nxt[poss]
print(ans // p)

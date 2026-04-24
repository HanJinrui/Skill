input()
S = 4 * [0]
e = 0
for c in input():
	S[e | ('r' != c) << 1] += 1
	e = not e
print(min(max(S[0], S[3]), max(S[1], S[2])))

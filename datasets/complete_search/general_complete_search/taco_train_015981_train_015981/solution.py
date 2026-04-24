g = [list(input()) for _ in range(10)]
words = input().split(';')

def solve(g, words, index):
	if index == len(words):
		return g
	word = words[index]
	for i in range(10):
		for j in range(10):
			if g[i][j] == '-' or g[i][j] == word[0]:
				for k in range(len(word)):
					if j + k >= 10 or g[i][j + k] not in ('-', word[k]):
						break
				else:
					g2 = [l[:] for l in g]
					for k in range(len(word)):
						g2[i][j + k] = word[k]
					res = solve(g2, words, index + 1)
					if res:
						return res
				for k in range(len(word)):
					if i + k >= 10 or g[i + k][j] not in ('-', word[k]):
						break
				else:
					g2 = [l[:] for l in g]
					for k in range(len(word)):
						g2[i + k][j] = word[k]
					res = solve(g2, words, index + 1)
					if res:
						return res
print('\n'.join((''.join(l) for l in solve(g, words, 0))))

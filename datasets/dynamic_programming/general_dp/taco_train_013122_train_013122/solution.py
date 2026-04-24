def distance(strings, ast, ach, zst, zch):
	if ast > zst:
		return 0 - distance(strings, zst, zch, ast, ach)
	dist = 0
	while ast != zst:
		dist += len(strings[ast]) - ach
		ast += 1
		ach = 0
	return dist + zch - ach

def search_back(strings, ast, ach, zst, zch, sthi, target):
	while zst >= max(ast, sthi - 1):
		s2 = strings[zst]
		while zch >= 0:
			if s2[zch] == target:
				if ast == zst and ach >= zch:
					return (-1, -1)
				return (zst, zch)
			zch -= 1
		zst -= 1
		zch = len(strings[zst]) - 1
	return (-1, -1)

def back(strings, st, ch):
	if ch <= 0:
		return (st - 1, len(strings[st - 1]) - 1)
	else:
		return (st, ch - 1)

def fwd(strings, st, ch):
	if ch + 1 >= len(strings[st]):
		return (st + 1, 0)
	else:
		return (st, ch + 1)

def count_subsequences(strings, counts, ast, ach, zst, zch, stlo, sthi):
	if ast >= zst:
		if ast > zst:
			return 1
		if ach > zch:
			return 1
		if ach == zch:
			if ast == stlo or ast == sthi:
				return 2
			else:
				return 1
	if (ast, ach, zst, zch, stlo, sthi) in counts:
		return counts[ast, ach, zst, zch, stlo, sthi]
	subsequences = 0
	aval = strings[ast][ach]
	(ast2, ach2) = fwd(strings, ast, ach)
	(mst, mch) = search_back(strings, ast, ach, zst, zch, sthi, aval)
	while mst != -1:
		mst2 = mst
		(mst, mch) = back(strings, mst, mch)
		subsequences += count_subsequences(strings, counts, ast2, ach2, mst, mch, ast, mst2)
		(mst, mch) = search_back(strings, ast, ach, mst, mch, sthi, aval)
	if ast2 <= stlo + 1:
		subsequences += count_subsequences(strings, counts, ast2, ach2, zst, zch, stlo, sthi)
	if stlo >= ast - 1 and ast >= sthi - 1:
		subsequences += 1
	counts[ast, ach, zst, zch, stlo, sthi] = subsequences % 1000000007
	return subsequences % 1000000007
for q in range(0, int(input())):
	num_strings = int(input())
	strings = list(map(lambda _: input().strip(), range(0, num_strings)))
	print(count_subsequences(strings, {}, 0, 0, num_strings - 1, len(strings[num_strings - 1]) - 1, -1, num_strings))

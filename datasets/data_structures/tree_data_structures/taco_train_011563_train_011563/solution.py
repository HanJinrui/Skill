def get_ints():
	return map(int, input().split())

def main():
	(_, m) = get_ints()
	s = [set() for _ in range(m)]
	(prev, score) = (-1, -1)
	for (index, dest) in enumerate(get_ints()):
		s[dest - 1].add(index)
		if prev != dest:
			score += 1
		prev = dest
	ans = [score]
	for _ in range(m - 1):
		(x, y) = get_ints()
		(x, y) = (x - 1, y - 1)
		target = x
		if len(s[x]) < len(s[y]):
			(x, y) = (y, x)
		for e in s[y]:
			if e - 1 in s[x]:
				score -= 1
			if e + 1 in s[x]:
				score -= 1
		for e in s[y]:
			s[x].add(e)
		s[target] = s[x]
		ans.append(score)
	print(*ans, sep='\n')
main()

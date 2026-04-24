def countDistinctSubstring(s):
	k = 1
	p = set()
	for i in range(len(s)):
		for j in range(i + 1, len(s) + 1):
			p.add(s[i:j])
	return len(p) + 1

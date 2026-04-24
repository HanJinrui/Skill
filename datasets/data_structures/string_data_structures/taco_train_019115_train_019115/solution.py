def kPangram(s, k):
	s = s.replace(' ', '')
	return 1 if 26 - len(set(s)) <= k and len(s) >= 26 else 0

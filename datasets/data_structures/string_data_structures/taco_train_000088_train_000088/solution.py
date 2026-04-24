def findSpecificPattern(Dict, pattern):
	a = []
	for i in Dict:
		if len(set(i)) == len(set(pattern)) and len(i) == len(pattern):
			a.append(i)
	return a

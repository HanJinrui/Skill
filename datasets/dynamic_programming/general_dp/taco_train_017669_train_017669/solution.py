def bestlastrotation(s, groups, letters, memos):
	if len(letters) < 3:
		return groups[0]
	mn = letters[0]
	mn2 = letters[1]
	mn3 = letters[2]
	lens = len(s)
	groups2 = []
	for g in groups:
		i = g
		while s[i] == mn:
			i = (i + 1) % lens
		if s[i] == mn2 and s[g - 1] != mn2:
			groups2.append([g, i])
	if len(groups2) == 0:
		return groups[0]
	if len(groups2) == 1:
		return groups2[0][0]
	for gg in groups2:
		j = gg[1]
		while s[j] == mn2 or s[j] == mn:
			j = (j + 1) % lens
		if s[j] != mn3:
			return gg[0]
		else:
			gg.append(j)
	if len(letters) < 4:
		return groups2[0][0]
	groupset = set((x[0] for x in groups2))
	ans = 0
	best = lens
	for g in groupset:
		s2 = (s[g:] + s[:g]).replace(mn, '')
		result = min_rotations(s2, memos)
		if best > result:
			best = result
			ans = g
	return ans

def min_rotations(s, memos):
	if s in memos:
		return memos[s]
	letters = sorted(set(s))
	mn = min(letters)
	ans = 0
	while mn != max(letters):
		i = 0
		while s[i] == mn:
			i += 1
		if i > 0:
			s = s[i:]
		groups = []
		for i in range(len(s)):
			if s[i] == mn and s[i - 1] != mn:
				groups.append(i)
		ans += len(groups)
		if len(groups) == 1:
			g = groups[0]
			s = s[g:] + s[:g]
		if len(groups) > 1:
			g = bestlastrotation(s, groups, letters, memos)
			s = s[g:] + s[:g]
		s = s.replace(mn, '')
		letters = letters[1:]
		mn = min(letters)
	memos[s] = ans
	return ans
q = int(input().strip())
for a0 in range(q):
	s = input().strip()
	print(min_rotations(s, dict()))

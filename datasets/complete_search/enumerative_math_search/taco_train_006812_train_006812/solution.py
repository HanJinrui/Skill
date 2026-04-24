for s in [*open(0)][1:]:
	print(9 * len(s) - 18 + int(s[0]) - ('.' < s.strip(s[0]) < s[0]))

for s in [*open(0)][1:]:
	t = set()
	i = 1
	for x in s[:-1]:
		if len((t := (t | {x}))) > 3:
			t = {x}
			i += 1
	print(i)

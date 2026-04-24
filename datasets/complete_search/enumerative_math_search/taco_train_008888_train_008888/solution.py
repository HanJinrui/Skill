for s in [*open(0)][2::2]:
	print((t := ({*'14689'} & {*s})) and '1\n' + t.pop() or '2\n' + ((t := ({*'25'} & {*s[1:]})) and s[0] + t.pop() or ((t := [x for x in s if s.count(x) > 1]) and 2 * t[0]) or s.replace('3', '')))

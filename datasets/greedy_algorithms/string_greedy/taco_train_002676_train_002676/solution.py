for k in [*open(0)][2::2]:
	print(k.find('LR') + 1 | len({*k}) - 3)

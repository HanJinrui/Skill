for i in [*open(0)][2::2]:
	print(len({*i.split()}))

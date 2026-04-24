import itertools
for i in range(int(input())):
	print(''.join( ch for ch,_ in itertools.groupby(input())))

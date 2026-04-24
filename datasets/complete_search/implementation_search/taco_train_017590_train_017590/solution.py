for i in [list(map(int, input().split() + input().split())) for j in range(int(input()))]:
	print(['NO', 'YES'][i.index(max(i)) + i.index(min(i)) == 3])

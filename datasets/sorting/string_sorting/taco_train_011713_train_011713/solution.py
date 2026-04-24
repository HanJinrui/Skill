n = int(input())
arr = [input().split() for i in range(n)]
for i in [['rat'], ['woman', 'child'], ['man'], ['captain']]:
	for j in arr:
		if j[1] in i:
			print(j[0])

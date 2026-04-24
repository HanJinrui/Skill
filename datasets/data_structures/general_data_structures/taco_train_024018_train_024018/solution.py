import bisect
col = []
for i in range(int(input())):
	bisect.insort_left(col, int(input()))
	mid = len(col) // 2
	values = col[mid - i % 2:mid + 1]
	print(sum(values) / len(values))

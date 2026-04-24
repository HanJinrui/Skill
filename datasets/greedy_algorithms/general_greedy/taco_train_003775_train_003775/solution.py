def lex_sort(N,arr):
	if N == 0 or not arr:
		return arr
	index = arr.index(min(arr[:N+1],key=int))
	return [arr[index]] + lex_sort(N-index,arr[:index] + arr[index+1:])
	
reps = int(input().split()[0])
for i in range(reps):
	N = int(input().split()[1])
	arr = input().split()
	print(' '.join(lex_sort(N,arr)))

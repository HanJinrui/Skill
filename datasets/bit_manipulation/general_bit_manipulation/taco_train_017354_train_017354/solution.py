def count_special(N):
	count = 0
	prev = 0
	curr = 3
	while(curr <= N):
		prev = curr
		curr = 2*prev + 1
		count += 1
	return count

T = int(input())
for t in range(T):
	N = int(input())
	count = count_special(N)
	print(count)

for i in range(int(input())):
	n = int(input())
	arr = input().split()
	ans = 0
	for i in arr:
		ans ^= int(i)
	if n & 1:
		ans = 0
	print('YES') if ans == 0 else print('NO')

n = int(input())
a = list(map(int, input().split()))
try:
	c = 1 << max(a).bit_length() - 1
	while min(a) >= c:
		a = [i - c for i in a]
		c = 1 << max(a).bit_length() - 1
	print(min((i ^ j for i in a for j in a if i < c and j >= c)))
except:
	print(0)

lst = ['North', 'East', 'South', 'West']
t = int(input())
for i in range(t):
	x = int(input())
	print(lst[x % 4])

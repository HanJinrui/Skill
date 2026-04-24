n = int(input())
c1 = input().count('1')
if c1 & 1:
	print('NO')
elif c1 == 0 and n & 1:
	print('NO')
else:
	print('YES')

n = int(input())
for i in range(n):
	n = int(input())
	A = input()
	B = input()
	print('YES' if A.count('1') == B.count('1') else 'NO')

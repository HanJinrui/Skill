(a, b) = map(lambda s: bin(int(s))[2:], input().split())
(a0, a1) = (a + '1', a.rstrip('0'))
if a == b or __import__('re').fullmatch(f'1*({a0}|{a1}|{a0[::-1]}|{a1[::-1]})1*', b):
	print('YES')
else:
	print('NO')

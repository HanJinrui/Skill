modulo = 10 ** 9 + 7
input()
a = map(int, input().split())
q = int(input())
s = sum(a) % modulo
for i in range(1, q + 1):
	s = s * 2 % modulo
	print(s)

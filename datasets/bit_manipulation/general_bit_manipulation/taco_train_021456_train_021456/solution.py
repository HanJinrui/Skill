(n, k) = map(int, input().split())
s = int(input(), 2)
s ^= s << 1
while k < n:
	s ^= s << k
	k *= 2
s &= 2 ** n - 1
print(format(s, '0' + str(n) + 'b'))

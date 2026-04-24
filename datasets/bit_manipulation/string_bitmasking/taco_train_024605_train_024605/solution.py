a = int(input())
b = [ord(i) - 97 for i in input()[::-1]]
c = [ord(i) - 97 for i in input()[::-1]]
it = b[0] + c[0]
s = []
for i in range(1, a):
	it += 26 * (b[i] + c[i])
	s.append(chr(it // 2 % 26 + 97))
	it //= 26
s.append(chr(it // 2 % 26 + 97))
s = ''.join(s[::-1])
print(s)

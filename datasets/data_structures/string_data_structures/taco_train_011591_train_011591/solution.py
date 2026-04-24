(t, m) = input().split()
d = {'_': ' '}
for i in range(0, 26):
	d[chr(i + 97)] = m[i]
m = m.upper()
for i in range(0, 26):
	d[chr(i + 65)] = m[i]
for _ in range(int(t)):
	s = input()
	ans = ''
	for i in s:
		ans += d.get(i, i)
	print(ans)

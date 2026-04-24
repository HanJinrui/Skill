import re
u = int
G = input
X = sorted
y = print
A = re.findall
a = u(G())
b = X([[u((i[0] or '+') + (i[1] or '1')), i[3]] for i in A('(\\+|-)?(\\d{0,4})(\\*)?(a\\+\\+|\\+\\+a)', G())])
z = 0
for i in b:
	if i[1] == 'a++':
		z += i[0] * a
	else:
		z += i[0] * (a + 1)
	a += 1
y(z)

def evaluate(a):
	c1 = a.count('1')
	c0 = a.count('0')
	n = len(a)
	A = (n - 1) // 2
	B = (n - 2) // 2
	if c1 <= A:
		return '00'
	if c0 <= B:
		return '11'
	p1 = a.rfind('1')
	p0 = a.rfind('0')
	if p0 < p1:
		return '01'
	else:
		return '10'
a = input()
x = []
x.append(evaluate(a.replace('?', '0')))
x.append(evaluate(a.replace('?', '1')))
n = len(a)
c1 = a.count('1')
c0 = a.count('0')
A = (n - 1) // 2
B = (n - 2) // 2
x.append(evaluate(a.replace('?', '0', B + 1 - c0).replace('?', '1')))
x.append(evaluate(a.replace('?', '1', A + 1 - c1).replace('?', '0')))
for ans in sorted(list(set(x))):
	print(ans)

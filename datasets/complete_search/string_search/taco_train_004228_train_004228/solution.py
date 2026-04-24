a = list(input())
b = list(input())
while a and b and (a[-1] == b[-1]):
	a.pop()
	b.pop()
print(len(a + b))

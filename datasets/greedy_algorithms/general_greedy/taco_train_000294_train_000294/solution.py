input()
a = input().strip().split()
b = input().strip().split()
count = 0
for el in a[:]:
	if el in b:
		a.remove(el)
		b.remove(el)
		count += 1
print(count + {1: 1, 0: -1}[bool(len(b))])

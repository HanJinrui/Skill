n = int(input())
ls = input().split()
st = []
for i in range(n):
	x = int(ls[i])
	while len(st) > 0 and x == st[-1]:
		x += 1
		st.pop()
	st.append(x)
print(len(st))
for x in st:
	print('{} '.format(x), end='')

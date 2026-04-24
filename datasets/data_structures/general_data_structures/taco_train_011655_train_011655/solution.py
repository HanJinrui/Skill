st = [[float('inf'), 0]]
input()
res = 0
for h in map(int, input().split()):
	while st[-1][0] < h:
		st.pop()
	if st[-1][0] == h:
		res += st[-1][1]
		st[-1][1] += 1
	else:
		st.append([h, 1])
print(res * 2)

input()
mx = 0
st = [(float('inf'), 0, 0)]
for (j, a) in enumerate(map(int, input().split()), 1):
	while st[-1][0] < a:
		i = st.pop()[2]
		mx = max(i * j, mx)
	i = st[-1][2] if st[-1][0] == a else st[-1][1]
	st.append((a, j, i))
print(mx)

(n, k) = map(int, input().split())
st = input()
s = set(st)
ans = 0
d = [0] * n
for i in s:
	for j in range(st.find(i), st.rfind(i) + 1):
		d[j] += 1
if max(d) > k:
	print('YES')
else:
	print('NO')

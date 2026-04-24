n = int(input())
(*a,) = map(int, input().split())
(*b,) = map(int, input().split())
(ans, s, k) = ([], 0, 0)
while b:
	x = b.index(a[k])
	b.remove(a[k])
	ans.append((x + k + 1, k + 1))
	s += x
	k += 1
print(s)
for i in ans:
	for j in range(i[0], i[1], -1):
		print(j - 1, j)

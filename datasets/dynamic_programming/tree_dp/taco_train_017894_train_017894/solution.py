(n, k, d) = map(int, input().split())
mat = [1]
sat = [1]
for i in range(1, n + 1):
	mat.append(sum(mat[max(i - d + 1, 0):]))
	sat.append(sum(sat[max(i - k, 0):]))
print((sat[-1] - mat[-1]) % 1000000007)

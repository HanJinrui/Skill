class Solution:

	def socialNetwork(self, arr, N):
		links = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
		for i in range(N - 1):
			links[i + 2][arr[i]] = 1
			for j in range(1, arr[i]):
				if links[arr[i]][j] != 0:
					links[i + 2][j] = links[i + 2][arr[i]] + links[arr[i]][j]
		ans = []
		for i in range(2, N + 1):
			for j in range(1, i):
				if links[i][j] != 0:
					ans.append(i)
					ans.append(j)
					ans.append(links[i][j])
		return ' '.join((str(a) for a in ans))
		1 < 2
		1 < 3 < 4

class Solution:

	def maximumToys(self, N, A, Q, Queries):
		tot = []
		for q in Queries:
			amt = q[0]
			ans = 0
			cnt = 0
			cost = list(A)
			l = len(q)
			for i in range(2, l):
				cost.remove(A[q[i] - 1])
			cost.sort()
			for i in cost:
				ans += i
				cnt += 1
				if ans > amt:
					ans -= i
					cnt -= 1
					break
			tot.append(cnt)
		return tot

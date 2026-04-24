class Solution:

	def generateNextPalindrome(self, num, n):
		num2 = num[:]
		for i in range(n // 2):
			num[n - 1 - i] = num[i]
		if num2 < num:
			return num
		curr = n // 2
		while curr >= 0 and num[curr] == 9:
			num[curr] = 0
			num[n - 1 - curr] = 0
			curr -= 1
		if curr < 0:
			ans = [0] * (n + 1)
			ans[0] = ans[-1] = 1
		else:
			num[curr] += 1
			num[n - 1 - curr] = num[curr]
			ans = num
		return ans

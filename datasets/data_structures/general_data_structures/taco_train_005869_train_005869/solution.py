class Solution:

	def findMaxDiff(self, arr, n):
		st = [-1]
		arr.append(0)
		ans = 0
		for i in range(len(arr)):
			while arr[st[-1]] > arr[i]:
				cur = arr[st.pop()]
				cur_ans = abs(arr[i] - arr[st[-1]])
				ans = max(ans, cur_ans)
			if len(st) > 1 and arr[st[-1]] == arr[i]:
				continue
			st.append(i)
		return ans

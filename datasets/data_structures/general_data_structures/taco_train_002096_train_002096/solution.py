class Solution:

	def FindElement(self, arr, N):
		max_ele = arr[0]
		li = [max_ele]
		for i in range(1, N):
			if max_ele >= arr[i]:
				if len(li) > 0:
					if li[0] >= arr[i]:
						li.clear()
			else:
				max_ele = arr[i]
				li.append(arr[i])
		return li[0] if len(li) > 0 else -1

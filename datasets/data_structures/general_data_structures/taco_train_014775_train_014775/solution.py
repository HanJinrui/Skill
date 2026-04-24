class Solution:

	def getAnswer(self, arr, answer, n):
		lis = arr.copy()
		dic = {}
		for i in arr:
			dic[i] = 1
		if n % 2 != 0:
			dic[arr[-1]] = 0
		while len(lis) > 1:
			j = 0
			mis = []
			while j + 1 < len(lis):
				if lis[j] < lis[j + 1]:
					mis.append(lis[j + 1])
				else:
					mis.append(lis[j])
				j += 2
			if len(lis) % 2 != 0:
				mis.append(lis[-1])
			lis = mis
			if len(lis) % 2 != 0:
				dic[lis[-1]] -= 1
			for i in lis:
				if i in dic:
					dic[i] += 1
		for i in range(n):
			answer[i] = dic[arr[i]]
		return answer

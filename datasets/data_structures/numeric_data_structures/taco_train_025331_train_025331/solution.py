primes = [2, 3]

class Solution:

	def primeMoney(self, arr, n):
		maxi = max(arr)
		i = primes[-1] + 2
		while maxi >= i:
			flag = True
			for item in primes:
				if i % item == 0:
					flag = False
					break
			if flag:
				primes.append(i)
			i += 2
		setti = set(primes)
		count = 0
		summa = 0
		last = 0
		temp_count = 0
		temp_summa = 0
		for item in arr:
			if item > last:
				temp_count += 1
				if item in setti:
					temp_summa += item
			else:
				if temp_count > count:
					count = temp_count
					summa = temp_summa
				elif temp_count == count:
					summa = max(summa, temp_summa)
				temp_count = 1
				if item in setti:
					temp_summa = item
				else:
					temp_summa = 0
			last = item
		if temp_count > count:
			count = temp_count
			summa = temp_summa
		elif temp_count == count:
			summa = max(summa, temp_summa)
		return (summa, count)

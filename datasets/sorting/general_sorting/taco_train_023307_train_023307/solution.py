def solve(arr):
	if len(arr) <= 1:
		return 0
	mid = len(arr) // 2
	left = arr[:mid]
	right = arr[mid:]
	count = 0
	count += solve(left)
	count += solve(right)
	(i, j, k) = (0, 0, 0)
	while i < len(left) and j < len(right):
		if left[i] > right[j]:
			count += len(left) - i
			arr[k] = right[j]
			j += 1
		else:
			arr[k] = left[i]
			i += 1
		k += 1
	while i < len(left):
		arr[k] = left[i]
		i += 1
		k += 1
	while j < len(right):
		arr[k] = right[j]
		j += 1
		k += 1
	return count

class Solution:

	def countSwaps(self, arr, n):
		return solve(arr)

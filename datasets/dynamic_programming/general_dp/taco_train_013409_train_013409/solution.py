def generate_sums(array):
	cur_sum = 0
	sums = [0] * len(array)
	for i in range(len(array)):
		cur_sum += array[i]
		sums[i] = cur_sum
	return sums

def dishdis(foods, cooks):
	cook = cooks.pop()
	previous = [1 if cook[0] <= food_count <= cook[1] else 0 for food_count in range(foods + 1)]
	previous_sums = generate_sums(previous)
	while cooks:
		cook = cooks.pop()
		current = [0] * (foods + 1)
		for i in range(0, foods + 1):
			interval_start = max(-1, i - cook[1] - 1)
			interval_end = i - cook[0]
			if interval_end < 0:
				current[i] = 0
			elif interval_start < 0:
				current[i] = previous_sums[interval_end]
			else:
				current[i] = previous_sums[interval_end] - previous_sums[interval_start]
		previous = current
		previous_sums = generate_sums(previous)
	return previous[foods] % 1000000007
for _ in range(int(input())):
	(foods, cook_count) = [int(x) for x in input().split()]
	cooks = [[int(x) for x in input().split()] for _ in range(cook_count)]
	print(dishdis(foods, cooks))

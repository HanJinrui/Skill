import sys
input_arr = [line.strip('\n') for line in sys.stdin]
found_max = 0
stack = []
for line in input_arr[1:]:
	entries = line.split(' ')
	if entries[0] == '1':
		value = int(entries[1])
		if found_max != 0:
			found_max = max(found_max, value)
		stack.append(value)
	elif entries[0] == '2':
		value = stack.pop()
		found_max = 0
	elif entries[0] == '3':
		if found_max == 0:
			found_max = max(stack)
		print(found_max)

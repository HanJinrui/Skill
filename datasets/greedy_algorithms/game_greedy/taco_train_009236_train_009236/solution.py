num_stacks = int(input())
answer = 0
array = []
for i in range(num_stacks):
	(a1, b1, a2, b2) = input().split(' ')
	a1 = int(a1)
	a2 = int(a2)
	b1 = int(b1)
	b2 = int(b2)
	if a1 + b1 >= a2 + b2:
		answer += a1 + a2
		array.append(a2 + b2)
		array.append(a1 + b1)
	elif a1 > b2:
		answer += a1 - b2
	elif b1 > a2:
		answer += a2 - b1
array.sort()
for i in range(0, len(array), 2):
	answer -= array[i]
print(answer)

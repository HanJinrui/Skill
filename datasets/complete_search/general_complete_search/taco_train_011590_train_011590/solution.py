import random
N = int(input())
in_put = input()
numbers = [int(x) for x in in_put.split()]
d = 101
operator = ['+', '-', '*']
listOp = [operator[random.randrange(0, len(operator), 1)] for i in range(0, N)]
listOp[0] = operator[0]
solution = False
while solution == False:
	result = 0
	for (i, op) in enumerate(listOp):
		if op == '+':
			result = result + numbers[i]
		elif op == '-':
			result = result - numbers[i]
		elif op == '*':
			result = result * numbers[i]
	if result % d == 0:
		solution = True
	else:
		for i in range(1, len(listOp)):
			listOp[i] = operator[random.randrange(0, len(operator), 1)]
out = str(numbers[0])
for i in range(1, len(listOp)):
	out = out + str(listOp[i]) + str(numbers[i])
print(out)

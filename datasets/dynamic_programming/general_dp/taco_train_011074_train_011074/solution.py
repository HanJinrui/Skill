import re
from functools import reduce
INPUT_PAT = re.compile('(-?\\d+)\\s*')

def smallest_expression(a, b):
	return (min(a[0] - b, a[0] + b, a[0] * b, a[1] * b), max(a[1] - b, a[1] + b, a[0] * b, a[1] * b))
num_examples = int(input())
for _ in range(num_examples):
	n = int(input())
	(a0, *a) = (int(i) for i in INPUT_PAT.findall(input()))
	print(reduce(smallest_expression, a, (a0, a0))[0])

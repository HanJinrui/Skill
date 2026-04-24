import math
from itertools import combinations_with_replacement

def find_SBN():
	if N in sqSet:
		return '1' * N
	ctr = N
	while ctr >= 0:
		for num in combinations_with_replacement([4, 9, 16, 25, 36, 49, 64, 81], N - ctr):
			s = ctr + sum(num)
			if s in sqSet:
				return '1' * ctr + ''.join([str(int(math.sqrt(_))) for _ in num])
		ctr -= 1
	return '-1'
T = int(input())
opList = []
sqSet = {i * i for i in range(9001)}
for x in range(T):
	N = int(input())
	opList.append(find_SBN())
print('\n'.join(opList))

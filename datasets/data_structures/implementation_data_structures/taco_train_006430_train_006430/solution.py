from bisect import *
from math import *
chefList = list()
diff = 0
for _ in range(int(input())):
	(age, value) = map(int, input().split(' '))
	chef = (age, value)
	index = bisect(chefList, chef)
	chefList.insert(index, chef)
	mid = ceil(len(chefList) / 2)
	if index < mid:
		diff -= value
		if len(chefList) % 2 == 0:
			diff += chefList[mid][1] * 2
	else:
		diff += value
		if len(chefList) % 2 == 1:
			diff -= chefList[mid - 1][1] * 2
	print(abs(diff))

import math


def solve(indx, sums, prev, curr):
	global noOfItem, cnts, wtMax, price, weight
	if indx == noOfItem or curr == cnts or sums == wtMax:
		return prev
	ans1 = solve(indx + 1, sums, prev, curr)
	ans2 = 0
	if (sums + weight[indx]) <= wtMax:
		ans2 = solve(indx + 1, sums + weight[indx], prev + price[indx], curr + 1)
	return max(ans1, ans2)


noOfDays = eval(input())
for d in range(noOfDays):
	noOfItem = eval(input())
	price = []
	weight = []
	for i in range(noOfItem):
		a, b = list(map(int, input().split()))
		price.append(a)
		weight.append(b)
	wtMax, cnts = list(map(int, input().split()))
	ans = solve(0, 0, 0, 0)
	if ans > 0:
		answ = ans
	else:
		answ = - 1

	print("For Day #{}:".format(d + 1))
	print(answ)

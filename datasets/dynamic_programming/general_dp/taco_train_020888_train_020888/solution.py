import sys
(ammount_prices, days_for_trading) = map(int, input().split())
stonks = []
for i in range(0, ammount_prices):
	price = int(sys.stdin.readline())
	stonks.append(price)

def get_max(days_for_trading, stonks):
	size_prices = len(stonks)
	if size_prices == 0 or size_prices == 1 or days_for_trading == 0:
		return 0
	if days_for_trading >= size_prices / 2:
		profit = 0
		for i in range(size_prices - 1):
			diff = stonks[i + 1] - stonks[i]
			if diff > 0:
				profit += diff
		return profit
	hold = days_for_trading * [float('-inf')]
	hold_prev = days_for_trading * [float('-inf')]
	release = days_for_trading * [float('-inf')]
	release_prev = days_for_trading * [float('-inf')]
	for price in stonks:
		for j in range(0, days_for_trading):
			if j == 0:
				hold[j] = max(-price, hold_prev[j])
			else:
				hold[j] = max(release_prev[j - 1] - price, hold_prev[j])
			release[j] = max(hold_prev[j] + price, release_prev[j])
		hold_prev = hold
		release_prev = release
	return release[-1]
print(get_max(days_for_trading, stonks))

import itertools

def initSquareCache():
	return list((i ** 2 for i in range(41)))

def enhancedDiff(purchasedLand, H, W, perfectStore, heightSub, widthSub):
	squareCache = initSquareCache()
	return min([[sum([sum([squareCache[abs(x - y)] for (x, y) in zip(purchasedLand[i + k][j:j + W], perfectStore[k])]) for k in range(H)]), i + 1, j + 1] for (i, j) in itertools.product(range(heightSub), range(widthSub))])
purchasedLand = []
[R, C] = map(int, input().split())
for i in range(R):
	purchasedLand += [list(map(int, input().split()))]
[H, W] = map(int, input().split())
perfectStore = []
for i in range(H):
	perfectStore += [list(map(int, input().split()))]
result = enhancedDiff(purchasedLand, H, W, perfectStore, R - H + 1, C - W + 1)
print('{0}\n{1} {2}'.format(*result))

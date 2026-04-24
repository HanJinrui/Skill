import heapq
FIBS = []
CUMSUMS = []
a = 0
b = 1
cumsum = 0
while cumsum < 10 ** 12:
	FIBS.append(b)
	cumsum += b
	CUMSUMS.append(cumsum)
	(a, b) = (b, a + b)

def solve(nums):
	s = sum(nums)
	if s not in CUMSUMS:
		return False
	nums = [-n for n in nums]
	heapq.heapify(nums)
	not_use = 0
	for ind in range(CUMSUMS.index(s), -1, -1):
		f = FIBS[ind]
		max_num = -heapq.heappop(nums)
		if f > max_num:
			return False
		max_num -= f
		heapq.heappush(nums, -not_use)
		not_use = max_num
	return True
n = int(input())
for _ in range(n):
	input()
	nums = list(map(int, input().strip().split()))
	if solve(nums):
		print('YES')
	else:
		print('NO')

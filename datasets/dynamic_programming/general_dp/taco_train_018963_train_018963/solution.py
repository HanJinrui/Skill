from copy import copy
from operator import itemgetter
ap = []
roots = []
saved_cost = dict()

class CostTree:

	def __init__(self, lower, upper):
		(self.lower, self.upper) = (lower, upper)
		self.points = self.sum = 0
		if self.lower == self.upper:
			self.L_branch = self.R_branch = None
		else:
			m = (self.lower + self.upper) // 2
			self.L_branch = CostTree(lower, m)
			self.R_branch = CostTree(m + 1, upper)

	def update(self, point):
		new = copy(self)
		new.points += 1
		new.sum += ap[point]
		if self.lower != self.upper:
			m = (new.lower + new.upper) // 2
			if point <= m:
				new.L_branch = new.L_branch.update(point)
			else:
				new.R_branch = new.R_branch.update(point)
		return new

def grow_cost_trees(p, n, k):
	all_points = []
	for (i, x) in enumerate(p):
		all_points.extend([(x[0], i), (x[1], i)])
	all_points.sort(key=itemgetter(0))
	(current, count, r) = (None, -1, [[] for i in range(n)])
	for i in range(2 * n):
		if all_points[i][0] != current:
			current = all_points[i][0]
			ap.append(current)
			count += 1
		r[all_points[i][1]].append(count)
	roots.append(CostTree(0, len(ap) - 1))
	for i in range(n):
		roots.append(roots[-1].update(r[i][0]).update(r[i][1]))

def cost(i, j):

	def cost_by_trees(i, j):
		b1 = roots[i]
		b2 = roots[j + 1]
		lower_sum = upper_sum = 0
		count_l = count_r = 0
		while True:
			if b1.L_branch is None:
				break
			if b2.L_branch.points - b1.L_branch.points >= j - i + 1 - count_l:
				upper_sum += b2.R_branch.sum - b1.R_branch.sum
				count_r += b2.R_branch.points - b1.R_branch.points
				(b1, b2) = (b1.L_branch, b2.L_branch)
			else:
				lower_sum += b2.L_branch.sum - b1.L_branch.sum
				count_l += b2.L_branch.points - b1.L_branch.points
				(b1, b2) = (b1.R_branch, b2.R_branch)
		return upper_sum - lower_sum + (count_l - count_r) * ap[b1.lower]
	if (i, j) not in saved_cost:
		saved_cost[i, j] = cost_by_trees(i, j)
	return saved_cost[i, j]

def find_least_cost(n, k):

	def recursive(left, right, bottom, top, comp):
		nonlocal row, next_row
		mid = (left + right) // 2
		for i in range(bottom, min(mid, top) + 1):
			temp = row[i] + cost(i + comp, mid + comp)
			if next_row[mid] is None or temp < next_row[mid]:
				next_row[mid] = temp
				L_limit = U_limit = i
			elif temp == next_row[mid]:
				U_limit = i
		if mid - left > 0:
			recursive(left, mid, bottom, L_limit, comp)
		if right - mid > 1:
			recursive(mid + 1, right, U_limit, top, comp)
		return (L_limit, U_limit)
	width = n - k + 1
	row = [cost(0, i) for i in range(width)]
	next_row = [None] * width
	for i in range(1, k - 1):
		(L_limit, _) = recursive(width - 1, width - 1, 0, width - 1, i)
		if width > 1:
			recursive(0, width - 1, 0, L_limit, i)
		(row, next_row) = (next_row, [None] * width)
	recursive(width - 1, width - 1, 0, width - 1, k - 1)
	return next_row[-1]

def solve():
	(n, k) = [int(i) for i in input().split()]
	point = []
	for _ in range(n):
		(i, j) = [int(i) for i in input().split()]
		point.append(tuple(sorted([i, j])))
	point.sort(key=lambda x: x[0] + x[1])
	grow_cost_trees(point, n, k)
	print(find_least_cost(n, k))
	return
solve()

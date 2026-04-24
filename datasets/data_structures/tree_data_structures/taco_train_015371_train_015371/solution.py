from collections import defaultdict

class Solution:

	def minTime(self, root, target):
		graph = defaultdict(list)
		stack = [(root, None)]
		while stack:
			(n, p) = stack.pop()
			if p:
				graph[p.data].append(n.data)
				graph[n.data].append(p.data)
			if n.left:
				stack.append((n.left, n))
			if n.right:
				stack.append((n.right, n))
		ans = -1
		seen = {target}
		queue = deque([target])
		while queue:
			for _ in range(len(queue)):
				u = queue.popleft()
				for v in graph[u]:
					if v not in seen:
						seen.add(v)
						queue.append(v)
			ans += 1
		return ans

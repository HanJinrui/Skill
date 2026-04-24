from heapq import heapify, heappush, heappop

def solve():
	n = int(input())
	text = [x - 97 for x in map(ord, input().strip())]
	graph = [[] for _ in range(n)]
	pos = [[] for _ in range(26)]
	for i in range(n - 1, -1, -1):
		pos[text[i]].append(i)
	heap = []
	in_degree = [0] * n
	for (x, neighbors) in zip(text, graph):
		i = pos[x].pop()
		if in_degree[i] == 0:
			heap.append((x, i))
		for (y, p) in enumerate(pos):
			if p and abs(x - y) != 1:
				j = p[-1]
				neighbors.append(j)
				in_degree[j] += 1
	heapify(heap)
	out = []
	while heap:
		(x, i) = heappop(heap)
		out.append(x + 97)
		for j in graph[i]:
			in_degree[j] -= 1
			if in_degree[j] == 0:
				heappush(heap, (text[j], j))
	print(''.join(map(chr, out)))

def main():
	n_cases = int(input())
	for _ in range(n_cases):
		solve()
main()

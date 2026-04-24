from abc import ABC, abstractmethod
import numpy as np

def get_int(source):
	return int(source())

def get_ints(source):
	return [int(x) for x in source().split(' ')]

def getline_from_std():
	return input()

class IOProcessing(ABC):

	@abstractmethod
	def read_test_case(self, source):
		pass

	@abstractmethod
	def process_test_case(self, tcase):
		pass

	def solve(self, input_type='from_std', output_type='to_std', input_path='', output_path='output.txt', tcase_handling='all'):
		ans = []
		if input_type == 'from_file':
			with open(input_path, 'r') as in_file:
				t = int(in_file.readline())
				for _ in range(t):
					tcase = self.read_test_case(in_file.readline)
					ans.append(self.process_test_case(tcase))
					if tcase_handling == 'single' and output_type == 'to_std':
						print(ans[-1])
		elif input_type == 'from_std':
			t = int(getline_from_std())
			for _ in range(t):
				tcase = self.read_test_case(getline_from_std)
				ans.append(self.process_test_case(tcase))
				if tcase_handling == 'single' and output_type == 'to_std':
					print(ans[-1])
		if output_type == 'to_file':
			with open(output_path, 'w') as output:
				for a in ans:
					output.write(a)
		elif output_type == 'to_std' and tcase_handling == 'all':
			for a in ans:
				print(a)
import numpy as np
import sys

class Ex_1_io(IOProcessing):

	def read_test_case(self, source):
		n = get_int(source)
		w = get_ints(source)
		edges = [[] for _ in range(n)]
		for _ in range(n - 1):
			(p, q) = get_ints(source)
			edges[p - 1].append(q - 1)
			edges[q - 1].append(p - 1)
		return (n, w, edges)

	def process_test_case(self, tcase):
		n = tcase[0]
		w = tcase[1]
		edges = tcase[2]
		inv = [0] * n
		wcount = [np.array([0, 0])] * n
		visited = [False] * n

		def dfs(v):
			visited[v] = True
			ans = 0
			wcount_new = np.array([1 - w[v], w[v]])
			wcount_children = []
			for v0 in edges[v]:
				if not visited[v0]:
					dfs(v0)
					ans += inv[v0]
					wcount_new += wcount[v0]
					wcount_children.append(wcount[v0])
			wcount_children.sort(key=lambda wc: -wc[0] / (wc[0] + wc[1]))
			sum_of_ones = 0
			sum_of_zeroes = 0
			for wc in wcount_children:
				ans += wc[0] * sum_of_ones
				sum_of_ones += wc[1]
				sum_of_zeroes += wc[0]
			if w[v] == 1:
				ans += sum_of_zeroes
			inv[v] = ans
			wcount[v] = wcount_new
		dfs(0)
		return inv[0]
sys.setrecursionlimit(1000000)
solution = Ex_1_io()
solution.solve(input_type='from_std', output_type='to_std', input_path='input.txt', output_path='output.txt', tcase_handling='all')

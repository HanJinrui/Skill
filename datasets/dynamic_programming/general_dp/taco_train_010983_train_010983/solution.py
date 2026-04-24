import sys
input = sys.stdin.readline
from sys import stdin, stdout
from math import ceil
import heapq

def main():
	for _ in range(int(input())):
		n = int(input())
		s = input().strip()
		if n == 1:
			print(0)
			continue
		m = s.count('1')
		j = 1
		pos = [-1] * (m + 1)
		for i in range(n):
			if s[i] == '1':
				pos[j] = i + 1
				j += 1
			if j > m:
				break
		dp = [[[10 ** 9 + 7, 10 ** 9 + 7] for i in range(m + 1)] for j in range(n + 1)]
		for i in range(n + 1):
			for j in range(m + 1):
				for filled in range(2):
					if j == 0:
						dp[i][j][filled] = 0
						continue
					if j > ceil(i / 2):
						continue
					if filled == 1:
						dp[i][j][filled] = dp[i - 1][j - 1][0] + abs(pos[j] - i)
					else:
						a = dp[i - 1][j][0]
						b = dp[i - 1][j][1]
						dp[i][j][filled] = min(a, b)
		ans = min(dp[n][m][0], dp[n][m][1])
		if ans == 10 ** 9 + 7:
			print('impossible')
		else:
			print(ans)

def main1():
	for _ in range(int(input())):
		n = int(input())
		s = input().strip()
		if n == 1:
			print(0)
			continue
		m = s.count('1')
		if m == 0:
			print(0)
			continue
		if m > (n + 1) // 2:
			print('impossible')
			continue
		j = 0
		pos = [-1] * m
		for i in range(n):
			if s[i] == '1':
				pos[j] = i
				j += 1
		heap = [0] * (m + 4)
		maxopt = n + 1 - 2 * m
		curropt = -10
		ans = 0
		for i in range(m):
			if -heap[0] <= pos[i] - 2 * i:
				curropt = min(maxopt, pos[i])
				heapq.heappush(heap, -(curropt - 2 * i))
			else:
				heapq.heappush(heap, -(pos[i] - 2 * i))
				curropt = -heap[0] + 2 * i
				heapq.heappop(heap)
				heapq.heappush(heap, -(pos[i] - 2 * i))
			ans += abs(curropt - pos[i])
			maxopt += 2
		print(ans)
main1()

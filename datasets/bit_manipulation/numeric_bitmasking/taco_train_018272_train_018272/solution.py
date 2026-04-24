from sys import stdout
import sys
for _ in range(int(input())):
	(n, k) = map(int, input().split())
	cum = 0
	for last in range(n):
		print(last ^ cum)
		stdout.flush()
		cum = last
		if sys.stdin.readline().strip() == '1':
			break

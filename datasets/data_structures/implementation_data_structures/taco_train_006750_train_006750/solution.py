from sys import stdin
input = stdin.readline
for _ in range(int(input())):
	input()
	tr = set(map(int, input().split()))
	input()
	dr = set(map(int, input().split()))
	input()
	ts = set(map(int, input().split()))
	input()
	ds = set(map(int, input().split()))
	print('yes' if ts.issubset(tr) and ds.issubset(dr) else 'no')

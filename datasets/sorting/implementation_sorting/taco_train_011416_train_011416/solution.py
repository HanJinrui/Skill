def main():
	from array import array
	from bisect import bisect
	from sys import stdin
	input = stdin.readline
	O = -1
	n = int(input())
	xr = []
	for i in range(n):
		(xi, ri) = map(int, input().split())
		xr.append((xi, ri ** 2, i))
	xr.sort()
	cur = 1
	res1 = 0
	res2 = array('i', (O,)) * n
	for _2 in range(int(input())):
		(x2, y) = map(int, input().split())
		bs = bisect(xr, (x2,))
		for i in (bs, bs - 1):
			if i < n:
				(xi, ri2, ii) = xr[i]
				if res2[ii] == O and (xi - x2) ** 2 + y ** 2 <= ri2:
					res1 += 1
					res2[ii] = cur
		cur += 1
	print(res1)
	print(*res2)
main()

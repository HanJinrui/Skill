import math

def solve(arr, n):
	even = []
	for x in arr:
		if x & 1 == 0:
			even.append(x)
	m = len(even)
	if m < math.ceil(n / 2):
		return 'NO'
	even.sort()
	result = even[0]
	for i in range(1, math.ceil(n / 2)):
		result = gcd(even[i], result)
		if result == 2:
			break
	if result == 2:
		return 'YES'
	return 'NO'

def gcd(a, b):
	if b == 0:
		return a
	return gcd(b, a % b)
t = int(input())
for _ in range(t):
	n = int(input())
	arr = list(map(int, input().split()))
	print(solve(arr, n))

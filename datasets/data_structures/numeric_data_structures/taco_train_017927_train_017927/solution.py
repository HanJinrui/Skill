from math import factorial
MOD = 10 ** 9 + 7

def getSum(n, arr):
	return sum(arr) * int('1' * n) * factorial(n - 1) % MOD

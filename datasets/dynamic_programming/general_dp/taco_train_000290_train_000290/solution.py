import sys
MOD = 998244353

def calc(arr):
	vars = []
	next = []
	vars = {i: 1 for i in arr[0]}
	for i in range(1, len(arr)):
		tot = sum(vars.values()) % MOD
		next = {}
		for num in arr[i]:
			cur = tot
			if num in vars:
				cur += MOD - vars[num]
			cur %= MOD
			next[num] = cur
		(next, vars) = (vars, next)
	return sum(vars.values()) % MOD

def main():
	arr = []
	N = int(sys.stdin.readline())
	for i in range(N):
		arr.append(list(map(int, sys.stdin.readline().strip().split())))
		arr[-1][0] = MOD
		arr[-1].sort()
		arr[-1].pop()
	Q = 450
	if N <= Q:
		ans = 0
		sign = False
		while len(arr) > 1:
			cur = calc(arr)
			if sign:
				cur = MOD - cur
			ans += cur
			ans %= MOD
			arr[0] = list(set(arr[0]).intersection(set(arr[-1])))
			arr[0].sort()
			del arr[-1:]
			sign = not sign
		print(ans)
	else:
		best = 10 ** 15
		mem = -1
		saved_set = []
		for i in range(N):
			prev = (i + N - 1) % N
			t = set(arr[i]).intersection(set(arr[prev]))
			sz = len(t)
			if sz < best:
				best = sz
				mem = i
				saved_set = list(t)
		arr = arr[mem:] + arr[:mem]
		ans = calc(arr)
		saved_set.sort()
		for val in saved_set:
			arr[0] = [val]
			arr[-1] = [val]
			ans += MOD - calc(arr)
			ans %= MOD
		print(ans)
main()

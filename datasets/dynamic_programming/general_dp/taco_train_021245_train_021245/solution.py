def solve(act, prev, N):
	global arr
	global dp
	global to
	if act >= N:
		return 0 if prev >= N else arr[prev]
	if dp[act][prev] == -1:
		answ = 10 ** 9
		v = max(arr[prev], arr[act]) + solve(act + 2, act + 1, N)
		if v < answ:
			answ = v
			to[act][prev] = (prev, act)
		if act + 1 < N:
			v = max(arr[prev], arr[act + 1]) + solve(act + 2, act, N)
			if v < answ:
				answ = v
				to[act][prev] = (prev, act + 1)
			v = max(arr[act], arr[act + 1]) + solve(act + 2, prev, N)
			if v < answ:
				answ = v
				to[act][prev] = (act, act + 1)
		dp[act][prev] = answ
	return dp[act][prev]
N = int(input())
arr = [int(x) for x in input().split()]
dp = [[-1 for i in range(N)] for j in range(N)]
to = [[[-1, -1] for i in range(N)] for j in range(N)]
answ = solve(1, 0, N)
print(answ)
la = [0, 1, 2]
act = 1
prev = 0
while act < N:
	print(to[act][prev][0] + 1, to[act][prev][1] + 1)
	la.remove(to[act][prev][0])
	la.remove(to[act][prev][1])
	prev = la[0]
	la.append(act + 2)
	la.append(act + 3)
	act += 2
if N % 2 == 1:
	print(la[0] + 1)

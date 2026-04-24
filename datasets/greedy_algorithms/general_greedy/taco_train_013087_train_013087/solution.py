from sys import stdin, stdout
(n, k) = map(int, stdin.readline().split())
value = int(stdin.readline())
prices = list(map(int, stdin.readline().split()))
used = {}
challengers = prices[:-1]
for i in range(n - 1):
	challengers[i] = (challengers[i], i)
challengers.sort(reverse=True)
ind = challengers[k - 1][1]
cnt = 0
for i in range(k):
	used[challengers[i][1]] = challengers[i][0]
	cnt += challengers[i][0]
for i in range(n - 1):
	if not i in used and value < cnt - used[ind] + prices[i]:
		stdout.write(str(i + 1))
		break
	elif i in used and value < cnt:
		stdout.write(str(i + 1))
		break
else:
	stdout.write(str(n))

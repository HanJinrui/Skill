(n, m) = map(int, input().split())
s = input()
sl = len(s)
if m:
	y = map(int, input().split())
else:
	y = []

def prefix_func(s):
	pi = [0] * len(s)
	for i in range(1, len(s)):
		j = pi[i - 1]
		while j > 0 and s[i] != s[j]:
			j = pi[j - 1]
		pi[i] = j + 1 if s[i] == s[j] else j
	return pi
pi = prefix_func(s)
good = [False] * sl
j = sl - 1
while j >= 0:
	good[j] = True
	j = pi[j] - 1
end = 0
s = 0
for x in y:
	if x > end:
		s += x - end - 1
	elif not good[end - x]:
		print('0')
		exit()
	end = x + sl - 1
s += max(0, n - end)
print(pow(26, s, 1000000007))

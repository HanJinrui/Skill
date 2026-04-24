def update(bit, i):
	while i < len(bit):
		bit[i] += 1
		i += i & -i

def getsum(bit, i):
	res = 0
	while i > 0:
		res += bit[i]
		i -= i & -i
	return res
n = int(input())
arr = list(map(int, input().split()))
d = {}
l = list(sorted(set(arr)))
ind = 1
for i in range(len(l)):
	d[l[i]] = ind
	ind += 1
l = [0] * n
r = [0] * n
t = 0
bit = [0] * (ind + 10)
update(bit, d[arr[0]])
for i in range(1, n):
	l[i] = getsum(bit, ind + 1) - getsum(bit, d[arr[i]])
	update(bit, d[arr[i]])
bit = [0] * (ind + 10)
for i in range(n - 1, -1, -1):
	r[i] = getsum(bit, d[arr[i]] - 1)
	update(bit, d[arr[i]])
ans = 0
for i in range(n):
	ans += l[i] * r[i]
print(ans)

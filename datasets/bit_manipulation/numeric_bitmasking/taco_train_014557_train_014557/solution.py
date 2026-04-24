base = [-1] * 60
how = [-1] * 60
who = [-1] * 60
n = int(input())
arr = list(map(int, input().split()))
x = 0
for a in arr:
	x ^= a
mapper = [-1] * 60
ind = 59
ind_start = bin(x).count('1') - 1
for bit in reversed(range(60)):
	if 1 << bit & x:
		mapper[bit] = ind_start
		ind_start -= 1
	else:
		mapper[bit] = ind
		ind -= 1
for i in range(len(arr)):
	temp = 0
	for bit in range(60):
		if 1 << bit & arr[i]:
			temp ^= 1 << mapper[bit]
	arr[i] = temp
for i in range(n):
	x = arr[i]
	temp_how = 0
	while x > 0:
		b = x.bit_length() - 1
		if who[b] != -1:
			temp_how ^= how[b]
			x = x ^ base[b]
		else:
			who[b] = i
			base[b] = x
			how[b] = temp_how | 1 << b
			break
x = 0
temp = 0
for bit in reversed(range(60)):
	if x & 1 << bit == 0 and who[bit] != -1:
		x ^= base[bit]
		temp ^= how[bit]
result = [1] * n
for j in range(60):
	if temp & 1 << j:
		result[who[j]] = 2
print(*result)

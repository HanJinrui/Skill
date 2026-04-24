k = 1
n = int(input())
while n % k == 0:
	k *= 3
print(n // k + 1)

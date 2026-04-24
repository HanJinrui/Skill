i = 1
n = int(input())
while int(bin(i)[2:]) <= n:
	i += 1
print(i - 1)

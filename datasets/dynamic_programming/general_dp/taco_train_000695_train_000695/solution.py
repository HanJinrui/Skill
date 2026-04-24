a = int(input(), 2)
b = int(input(), 2)
print(sum((a ^ b << i for i in range(314160))) % 1000000007)

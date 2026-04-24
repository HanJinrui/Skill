n = int(input())
z = bin(n)[3:].count('0')
print(2 ** z)

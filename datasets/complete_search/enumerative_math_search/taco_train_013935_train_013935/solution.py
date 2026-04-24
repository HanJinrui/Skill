exec('a,b,c=' + 'int(input()),' * 3)
print(max(a + b + c, a * b * c, (a + b) * c, a * (b + c)))

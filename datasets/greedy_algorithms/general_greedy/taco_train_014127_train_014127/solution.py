x = input()
y = x.count('1')
print(len(x) + x.rfind('1') - y + 2 * (y > 1))

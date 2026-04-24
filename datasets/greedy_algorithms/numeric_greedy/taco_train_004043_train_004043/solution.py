a = input()
z = max(0, a.find('0'))
print(a[:z] + a[z + 1:])

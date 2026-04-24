i = int(input()) - 1
s = input().split()
while s[i] == s[0] == s[~i]:
	i -= 1
print(i)

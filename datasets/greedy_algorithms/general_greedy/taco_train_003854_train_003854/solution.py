k = int(input())
l = sorted(map(int, input()))
i = 0
su = sum(l)
while su < k:
	su += 9 - l[i]
	i += 1
print(i)

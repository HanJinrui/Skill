import collections
for _ in range(int(input())):
	print(int(input()) - collections.Counter([a // 2 for a in list(map(int, input().split()))]).most_common(1)[0][1])

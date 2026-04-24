n = int(input())
a = list(map(int, input().split()))
for i in range(int(input())):
	(w, h) = map(int, input().split())
	k = max(a[0], a[w - 1])
	a[0] = k + h
	print(k)

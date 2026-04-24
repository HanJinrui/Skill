n = int(input().strip())
cal = sorted(map(int, input().split()))
res = 0
for c in cal:
	res = res * 2 + c
print(res)

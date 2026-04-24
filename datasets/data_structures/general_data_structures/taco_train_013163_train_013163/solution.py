(N, Q) = [int(i) for i in input().strip().split()]
nums = [int(i) for i in input().strip().split()]
q = 0
temp = nums[:]
out = []
end = 1
primeList = [x for x in range(2, 10000) if all((x % y != 0 for y in range(2, x)))]
while q < Q:
	end = end * -1
	valTemp = []
	for n in temp[::end]:
		if not n % primeList[q]:
			valTemp.append(n)
			temp.remove(n)
	out += valTemp[::-1]
	q += 1
for item in out:
	print(item)
for item in temp[::end * -1]:
	print(item)

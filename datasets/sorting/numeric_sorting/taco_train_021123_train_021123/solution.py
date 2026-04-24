n = int(input())
a = list(map(int,input().split(' ')))
avg = sum(a)/n
p = a[0]-avg
b = [p]
for x in a[1:]:
	p = p + x -avg
	b.append(p)
b.sort()
mid = b[len(b)/2]
total = sum([abs(x-mid) for x in b])
print(total)

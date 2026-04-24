n = int(input())
a = (*map(int, input().split()),)
r = ''
i = p = 0
j = n - 1
while i <= j and max(a[i], a[j]) > p:
	if a[j] < p or a[j] >= a[i] > p:
		r += 'L'
		p = a[i]
		i += 1
	else:
		r += 'R'
		p = a[j]
		j -= 1
print(len(r), r)

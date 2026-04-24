t = int(input())
for ii in range(t):
	d_chef = {}
	d_boy = {}
	(n, k, p) = map(int, input().split())
	d_chef = set({int(input().split()[1]) for j in range(k)})
	d_boy = set({int(input().split()[1]) for j in range(p)})
	r = 'Yes'
	if not d_boy.issubset(d_chef):
		r = 'No'
	print(r)

d = {'00': [], '01': [], '10': [], '11': []}
n = int(input())
for i in range(n):
	(x, p) = input().split()
	d[x].append(int(p))
for key in d.keys():
	d[key].sort(reverse=True)
t = '01' if len(d['01']) <= len(d['10']) else '10'
t1 = '01' if t == '10' else '10'
ans = 0
ans += sum(d['11']) + sum(d[t]) + sum(d[t1][:len(d[t])])
e = len(d['11'])
l1 = sorted(d[t1][len(d[t]):] + d['00'], reverse=True)
ans += sum(l1[:e])
print(ans)

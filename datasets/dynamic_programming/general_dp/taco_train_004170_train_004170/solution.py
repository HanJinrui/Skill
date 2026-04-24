t=int(input())
for i in range(0,t):
	n = int(input())
	d=[]
	d.append(0)
	d.append(0)
	d.append(1)
	f=[]
	f.append(0)
	f.append(1)
	f.append(1)
	for i in range(3, n):
		f.append((f[i-1] + f[i-2])%1000000007)
	for i in range(3, n+1):
		d.append((d[i-1] + d[i-2] + f[i-1]) % 1000000007)
	print(d[n])

n = input().strip()
l = len(n)
p = [-1] * l
u = [0] * 10
p[0] = 0
id = 0
c1 = [0]
c2 = 0
while c2 < l:
	n2 = c1[c2]
	if u[int(n[n2])] == 0:
		for j in range(l):
			if p[j] < 0 and n[j] == n[n2]:
				p[j] = p[n2] + 1
				c1.append(j)
		u[int(n[n2])] = 1
	if n2 > 0 and p[n2 - 1] < 0:
		p[n2 - 1] = p[n2] + 1
		c1.append(n2 - 1)
	if n2 < l - 1 and p[n2 + 1] < 0:
		p[n2 + 1] = p[n2] + 1
		c1.append(n2 + 1)
	c2 += 1
print(p[-1])

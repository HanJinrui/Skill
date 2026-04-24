store = []

def inspect(j, sp):
	p = 1
	while '_' + j[0:p] in sp and p < len(j):
		p += 1
	store.append(j[0:p])
flag = 0
sn = []
sp = '_'
k = int(input())
for i in range(k):
	s1 = input()
	s1 = s1.split()
	if s1[0] is '+':
		sp += s1[1]
		sp += '_'
	else:
		sn.append(s1[1])
for j in sn:
	if '_' + j in sp:
		print(-1)
		flag = 1
		break
	else:
		inspect(j, sp)
if flag is not 1:
	store = sorted(set(store))
	print(len(store))
	for m in store:
		print(m)

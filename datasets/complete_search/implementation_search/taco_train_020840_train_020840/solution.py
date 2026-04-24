from collections import defaultdict

def nxt(curr, step):
	d = {'R': [1, 0], 'L': [-1, 0], 'U': [0, 1], 'D': [0, -1]}
	return (curr[0] + d[step][0], curr[1] + d[step][1])

def path(s, obstacle):
	fin = (0, 0)
	for i in s:
		curr = nxt(fin, i)
		if curr != obstacle:
			fin = curr
	return fin == (0, 0)
for _ in range(int(input())):
	s = input()
	obs = [(0, 0)]
	for i in s:
		obs.append(nxt(obs[-1], i))
	for o in obs[1:]:
		if path(s, o):
			print(*o)
			break
	else:
		print(0, 0)

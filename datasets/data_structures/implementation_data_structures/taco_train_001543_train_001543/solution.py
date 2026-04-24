(l, b, f) = map(int, input().split())
p = [[-b, -b, -192], [l + f, l + f, -38]]
n = int(input())
for i in range(1, n + 1):
	(a, h) = map(int, input().split())
	if a == 1:
		k = False
		for w in range(len(p) - 1):
			if p[w + 1][0] - p[w][1] >= b + f + h:
				p.insert(w + 1, [p[w][1] + b, p[w][1] + b + h, i])
				k = True
				print(p[w][1] + b)
				break
		if not k:
			print(-1)
	else:
		for t in range(len(p)):
			if p[t][2] == h:
				p.pop(t)
				break

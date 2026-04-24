(n, m) = map(int, input().split())
sp = set(input().split())
posts = []
for x in range(m):
	posts.append(input().split())
posts.sort(key=lambda x: int(x[1]), reverse=True)
for p in posts:
	if p[0] in sp:
		print(p[2])
for p in posts:
	if p[0] not in sp:
		print(p[2])

import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
(n, q) = map(int, input().split())
pos = [i for i in range(n)]
(cnt, temp, flag) = (0, [0, 0], 0)
for _ in range(q):
	p = list(map(int, input().split()))
	if p[0] == 1:
		x = (n + p[1]) % n
		cnt = cnt + x
		flag = flag ^ x % 2
	else:
		if flag != 0:
			temp[0] = temp[0] - 1
			temp[1] = temp[1] + 1
		else:
			temp[0] = temp[0] + 1
			temp[1] = temp[1] - 1
		flag = flag ^ 1
ans = [0 for i in range(n)]
for i in range(n):
	ans[(pos[i] + cnt + temp[i % 2]) % n] = i + 1
sys.stdout.write(' '.join(map(str, ans)))

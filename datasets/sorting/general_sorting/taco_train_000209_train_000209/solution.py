(N, K) = map(int, input().split())
l = list(map(int, input().split()))
l1 = []
can_swap = [0] * N
for i in range(N):
	if i + K < N - 1 or i - K > 0:
		can_swap[i] = 1
		l1.append(l[i])
l1.sort()
x = 0
for i in range(N):
	if can_swap[i]:
		l[i] = l1[x]
		x += 1
print(*l)

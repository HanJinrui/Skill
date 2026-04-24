(n, m) = map(int, input().split())
arr = [int(i) for i in input().split()]
sumo = sum(arr)
no = m
for i in range(m):
	input()
q = int(input())
for i in range(q):
	s = input()[0]
	if s == '+':
		no += 1
	elif s == '-':
		no -= 1
	else:
		print(sumo + 2 * no - n * (n - 1) // 2)

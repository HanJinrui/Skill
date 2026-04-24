def height(A, n):
	a = []
	mn = 1000000000.0 + 1
	mx = -1
	for i in range(n - 1):
		if A[i] < mn:
			mn = A[i]
		if A[i] > mx:
			mx = A[i]
		a.append(mx - mn)
	return a

def sort(L):
	return sorted(L, key=lambda x: x[0])

def fun(A, n):
	l2 = []
	for i in range(n):
		l2.append(A[i][1])
	h1 = height(l2, n)
	h2 = height(l2[::-1], n)
	h2 = h2[::-1]
	area = 1e+19 + 1
	for i in range(n - 1):
		temp = h1[i] * (A[i][0] - A[0][0]) + h2[i] * (A[-1][0] - A[i + 1][0])
		if temp < area:
			area = temp
	if area == 1e+19:
		return 0
	else:
		return area
for i in range(int(input())):
	n = int(input())
	(Lx, Ly) = ([], [])
	for i in range(n):
		(a, b) = map(int, input().split())
		Lx.append([a, b])
		Ly.append([b, a])
	Lx = sort(Lx)
	Ly = sort(Ly)
	area1 = fun(Lx, n)
	area2 = fun(Ly, n)
	print(min(area1, area2))

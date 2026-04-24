def count(points):
	points.sort()
	record = set(points)
	sol = 0
	for i in range(len(points)):
		for j in range(i + 1, len(points)):
			(x1, y1) = points[i]
			(x2, y2) = points[j]
			if y2 > y1:
				dx = abs(y2 - y1)
				dy = abs(x2 - x1)
				p3 = (x1 + dx, y1 - dy)
				p4 = (x2 + dx, y2 - dy)
				if p3 in record and p4 in record:
					sol += 1
	return sol
t = int(input())
for i in range(t):
	N = int(input())
	points = []
	for s in range(N):
		temp = input().split()
		points.append((int(temp[0]), int(temp[1])))
	print(count(points))

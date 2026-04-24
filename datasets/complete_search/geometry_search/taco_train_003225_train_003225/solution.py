def main():
	num_x = []
	num_y = []
	for i in range(3):
		(x, y) = map(int, input().split())
		num_x.append((x, y))
		num_y.append(y)
	num_x.sort()
	num_y.sort()
	ans_list = []
	x = num_x[1][0]
	y = num_y[1]
	for j in range(3):
		ans_list.append((x, y, num_x[j][0], y))
		ans_list.append((num_x[j][0], y, num_x[j][0], num_x[j][1]))
	k = 0
	for i in ans_list:
		if i[0] != i[2] or i[1] != i[3]:
			k += 1
	print(k)
	for i in ans_list:
		if i[0] != i[2] or i[1] != i[3]:
			print(*i)
for _ in range(1):
	main()

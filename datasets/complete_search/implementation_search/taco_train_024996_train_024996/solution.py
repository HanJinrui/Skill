for t in range(int(input())):
	(xk, yk) = map(int, input().split())
	(x1, y1) = map(int, input().split())
	(x2, y2) = map(int, input().split())
	if (xk == 1 or xk == 8) and (abs(xk - x1) == 1 or abs(xk - x2) == 1) and (abs(y1 - yk) != 1) and (abs(y2 - yk) != 1) and (y1 != y2):
		print('YES')
	elif (yk == 1 or yk == 8) and (abs(yk - y1) == 1 or abs(yk - y2) == 1) and (abs(x1 - xk) != 1) and (abs(x2 - xk) != 1) and (x1 != x2):
		print('YES')
	else:
		print('NO')

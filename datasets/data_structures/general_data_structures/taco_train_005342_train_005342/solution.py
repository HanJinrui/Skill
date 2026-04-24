heap = []
try:
	b = input()
	mini = None
	while True:
		x = input().split(' ')
		if x[0] == '1':
			heap.append(int(x[1]))
			if mini == None or int(x[1]) < mini:
				mini = int(x[1])
		elif x[0] == '2':
			heap.remove(int(x[1]))
			if int(x[1]) == mini and heap != []:
				mini = min(heap)
			elif heap == []:
				mini = None
		elif x[0] == '3':
			print(mini)
except:
	pass

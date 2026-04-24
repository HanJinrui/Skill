minup = input('')
L = minup.split(' ')
n = int(L[0])
k = int(L[1])
location = []
value = []
for i in range(n):
	a = input('')
	L = a.split(' ')
	location.append(int(L[0]))
	value.append(int(L[1]))
if n <= 3500:
	chasm = [0, 0]
	user = 0
	values = 0
	for i in range(n - k):
		values += value[i]
		user += values * (location[i + 1] - location[i])
		chasm.append(user)
	chasm = chasm + [0] * (n + 1 - len(chasm))
	location = [float('-inf')] + location
	value = [0] + value
	y = k - 1

	def roundi(a, b, tally, chunk, location=location, value=value):
		if luke[a][b] != -1:
			return luke[a][b]
		else:
			Sum = chunk
			for p in range(tally + 1, b):
				worth = value[p]
				if location[p] - location[a] <= location[b] - location[p]:
					tally = p
					chunk += worth * (location[p] - location[a])
					Sum = chunk
				else:
					Sum += worth * (location[b] - location[p])
			(luke[a][b], talisman[a][b], sun[a][b]) = (Sum, tally, chunk)
			return Sum
	luke = [[-1 for i in range(n + 1)] for j in range(n + 1)]
	talisman = [[j for i in range(n + 1)] for j in range(n + 1)]
	sun = [[0 for i in range(n + 1)] for j in range(n + 1)]
	charlie = [chasm, [0 for i in range(n + 1)]]
	xani = 1
	for i in range(2, k + 1):
		xani += 1
		begin = i - 1
		for j in range(i, n - y + xani):
			high = float('inf')
			for x in range(begin, j):
				tally = talisman[x][j - 1]
				chunk = sun[x][j - 1]
				z = roundi(x, j, tally, chunk) + charlie[0][x]
				if high >= z:
					index = x
					high = z
			charlie[1][j] = high
			begin = index
		(charlie[0], charlie[1]) = (charlie[1], charlie[0])
	zigzag = [[0], []]
	for i in range(k + 1, n + 1):
		zigzag[1] = [zigzag[0][x] + (location[i] - location[k + x]) * value[i] for x in range(len(zigzag[0]))]
		zigzag[1] += [charlie[0][i]]
		(zigzag[1], zigzag[0]) = (zigzag[0], zigzag[1])
	print(min(zigzag[0]))
else:
	chasm = [0, 0]
	user = 0
	values = 0
	for i in range(n - k):
		values += value[i]
		user += values * (location[i + 1] - location[i])
		chasm.append(user)
	chasm = chasm + [0] * (n + 1 - len(chasm))
	chasmal = chasm[:]
	location = [float('-inf')] + location
	value = [0] + value
	y = k - 1

	def roundi(a, b, location=location, value=value):
		if luke[a][b] != -1:
			return luke[a][b]
		else:
			Sum = sum((value[p] * min(location[p] - location[a], location[b] - location[p]) for p in range(a + 1, b)))
			luke[a][b] = Sum
			return Sum
	luke = [[-1 for i in range(n + 1)] for j in range(n + 1)]
	charlie = [chasm, [0 for i in range(n + 1)]]
	xani = 1
	for i in range(2, k + 1):
		xani += 1
		begin = i - 1
		for j in range(i, n - y + xani):
			high = float('inf')
			for x in range(begin, j):
				if high >= charlie[0][x] + roundi(x, j):
					index = x
					high = charlie[0][x] + roundi(x, j)
			charlie[1][j] = high
			begin = index
		(charlie[0], charlie[1]) = (charlie[1], charlie[0])
	zigzag = [[0], []]
	for i in range(k + 1, n + 1):
		zigzag[1] = [zigzag[0][x] + (location[i] - location[k + x]) * value[i] for x in range(len(zigzag[0]))]
		zigzag[1] += [charlie[0][i]]
		(zigzag[1], zigzag[0]) = (zigzag[0], zigzag[1])
	print(min(zigzag[0]))

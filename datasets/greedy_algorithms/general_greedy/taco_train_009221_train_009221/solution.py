for t in range(int(input())):
	A = sorted(tuple(map(int, input().split()))[1:])
	teams = {}
	for n in A:
		if n - 1 in teams:
			new_size = teams[n - 1][-1] + 1
			teams[n - 1].pop()
			if not teams[n - 1]:
				del teams[n - 1]
			if n in teams:
				teams[n].append(new_size)
				teams[n].sort(reverse=True)
			else:
				teams[n] = [new_size]
		elif n in teams:
			teams[n].append(1)
		else:
			teams[n] = [1]
	minimum = len(A)
	for v in teams.values():
		minimum = min(minimum, *v)
	print(minimum)

for _ in range(int(input())):
	l = int(input())
	seq = [int(i) % 2 for i in input().split()]
	if not any(seq):
		print(-1)
	else:
		count = [[], []]
		k = 0
		for i in range(l):
			count[k % 2].append(i)
			if i < l - 1 and seq[i] == seq[i + 1]:
				k += 1
		min = count[0] if len(count[0]) <= len(count[1]) else count[1]
		print(len(min))
		for i in min:
			seq[i] = -1
			print(i + 1, 1 + seq.index(1))

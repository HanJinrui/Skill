s = input() + 'X' * int(input())
for v in range(len(s) - len(s) % 2, 0, -2):
	for i in range(len(s) - v + 1):
		if all((s[j + v // 2] in ('X', s[j]) for j in range(i, i + v // 2))):
			(print(v), exit())

for _ in range(int(input())):
	n = int(input())
	s = input()
	cnt = sum((1 for i in range(n - 1) if s[i] == s[i + 1]))
	print('Uttu' if not cnt % 3 else 'JJ')

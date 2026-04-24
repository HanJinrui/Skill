for _ in range(int(input())):
	n = int(input())
	s = input()
	t = input()
	print(min(s.count('1'), t.count('1'), n // 2))

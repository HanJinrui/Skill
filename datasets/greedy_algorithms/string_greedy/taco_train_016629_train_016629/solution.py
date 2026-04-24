for _ in [0] * int(input()):
	input()
	s = input()
	(x, y) = (int(s[0]), int(s[1:]))
	print(('NO', f'YES 2 {x} {y}')[x < y])

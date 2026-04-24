for _ in range(eval(input())):
	text = input()
	pos = 0
	output = ''
	for c in text:
		move = (ord(c) - ord('a') - pos) % 26 
		output += str(move if move <= 13 else move - 26) + ' '
		pos = pos + move
	print(output[:-1])

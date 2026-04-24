d = int(input()) + 1
while len(set(str(d))) < 4:
	d += 1
print(d)

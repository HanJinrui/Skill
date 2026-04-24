NOTES = 'C C# D D# E F F# G G# A B H'.split()
(a, b, c) = sorted(map(NOTES.index, input().split()))
(x, y) = (b - a, c - b)
if (x, y) in ((3, 5), (4, 3), (5, 4)):
	print('major')
elif (x, y) in ((3, 4), (4, 5), (5, 3)):
	print('minor')
else:
	print('strange')

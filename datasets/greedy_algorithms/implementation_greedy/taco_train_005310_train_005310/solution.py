def main():
	l = [x == '7' for (x, y) in zip(input(), input()) if x != y]
	x = sum(l)
	print(max(x, len(l) - x))
main()

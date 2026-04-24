(X, Y) = map(float, input().split())
X = int(X)
if X + 0.5 <= Y and X % 5 == 0:
	print(float(Y - X - 0.5))
else:
	print(float(Y))

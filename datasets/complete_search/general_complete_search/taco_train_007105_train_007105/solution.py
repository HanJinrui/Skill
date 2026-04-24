R = lambda : map(int, input().split())
(t,) = R()
while t:
	t -= 1
	(W, H) = R()
	(u, v, x, y) = R()
	(w, h) = R()
	print(max(0, min(l)) if (l := ([w - u, w - W + x] * (w + x - u <= W) + [h - v, h - H + y] * (h + y - v <= H))) else -1)

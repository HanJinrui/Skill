exec('a,b,c,d,n=' + 'int(input()),' * 5)
if d < c:
	(a, b, c, d) = (b, a, d, c)
print(max(0, n - a * (c - 1) - b * (d - 1)), [n // c, a + (n - a * c) // d][n > a * c])

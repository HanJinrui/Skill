z = input
(a, b, c) = (int(z()), int(z()), int(z()) * 5)
print(min(((a - i) % b for i in range(0, a + 1, c))))

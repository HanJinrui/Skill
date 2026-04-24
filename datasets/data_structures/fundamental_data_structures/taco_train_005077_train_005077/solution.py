get_mean = lambda a, x, y: (1 < x <= len(a) >= y > 1) - 1 or (sum(a[:x]) / x + sum(a[-y:]) / y) / 2

p = tuple(((ord(s[0]) - ord('a'), int(s[1]) - 1) for s in (input() for i in range(2))))
print(sum(((i, j) not in p and i != p[0][0] and (j != p[0][1]) and all((sorted((abs(i - pi[0]), abs(j - pi[1]))) != [1, 2] for pi in p)) for i in range(8) for j in range(8))))

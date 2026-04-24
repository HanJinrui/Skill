c = input()
print((len(c) - (c == c[::-1])) * (len(set(c)) > 1))

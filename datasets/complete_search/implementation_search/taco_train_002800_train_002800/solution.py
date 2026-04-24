z = input
r = range
d = [s for s in (z() for _ in r(int(z()))) if len(set(s)) <= 2]
print(max((sum((len(s) for s in d if set(s) <= {chr(i), chr(j)})) for i in r(97, 123) for j in r(i, 123))))

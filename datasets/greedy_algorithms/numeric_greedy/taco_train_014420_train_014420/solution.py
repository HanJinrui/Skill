i = input
i()
a = {*map(int, i().split())}
print(sum((all((x % y for y in a - {x})) for x in a)))

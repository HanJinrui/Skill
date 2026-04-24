(_, s) = (input(), set(input()))
print(('NO', 'YES')[all((set(t) & s for t in '0147 0369 079 123'.split()))])

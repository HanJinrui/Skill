q = ''
exec('q+=input();' * int(input()))
print('YES' if q == q[::-1] else 'NO')

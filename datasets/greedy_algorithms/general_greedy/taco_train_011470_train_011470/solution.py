(x, y, z) = map(int, input().split())
c = z + abs(x - y) and '?'
print(f'{c}+-'[(x > y + z) + 2 * (y > x + z)])

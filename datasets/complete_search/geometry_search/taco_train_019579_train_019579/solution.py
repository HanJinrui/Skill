(x, y, z) = map(int, input().split())
(x1, y1, z1) = map(int, input().split())
a = list(map(int, input().split()))
print(a[0] * (y < 0) + a[1] * (y > y1) + a[2] * (z < 0) + a[3] * (z > z1) + a[4] * (x < 0) + a[5] * (x > x1))

(N, H, x) = map(int, input().split())
T = map(int, input().split())
print('YES') if x + max(T) >= H else print('NO')

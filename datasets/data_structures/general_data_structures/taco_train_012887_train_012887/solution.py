ints = lambda : set(map(int, input().split()))
A = ints()
print(all((A >= ints() for i in range(int(input())))))

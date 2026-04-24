(n, k) = map(int, input().split())
a = input().split()
print(sum([min([a[i::k].count(d) for d in '12']) for i in range(k)]))

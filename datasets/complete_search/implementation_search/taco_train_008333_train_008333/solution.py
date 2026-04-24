b = int(input().split()[1])
c = input()
print(['YES', 'NO'][max((c.count(i) for i in set(c))) > b])

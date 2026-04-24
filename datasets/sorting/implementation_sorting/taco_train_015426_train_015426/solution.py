t = sorted((input() for i in range(int(input()))))
print(['NO', 'YES\n' + t[0] + ' ' + t[-1]][len(t) // 2 == t.count(t[0]) == t.count(t[-1])])

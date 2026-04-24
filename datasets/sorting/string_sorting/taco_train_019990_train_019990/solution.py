sl = sorted([input() for i in range(int(input()))], key=len)
print(('NO', '\n'.join(['YES'] + sl))[all((x in y for (x, y) in zip(sl, sl[1:])))])

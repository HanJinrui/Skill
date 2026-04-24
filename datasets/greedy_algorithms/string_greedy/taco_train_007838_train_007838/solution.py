I = input
e = '02468'
exec(int(I()) * 'I();s=I().strip(e);print(s[sum(map(int,s))%2:].strip(e)or-1);')

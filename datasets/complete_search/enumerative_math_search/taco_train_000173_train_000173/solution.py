R = lambda : sorted(map(int, input().split()))
(t,) = R()
exec(t * "a,b=R();c,d=R();print('NYOE S'[b==d==a+c::2]);")

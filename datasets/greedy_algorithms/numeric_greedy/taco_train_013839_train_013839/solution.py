R = lambda : map(int, input().split())
(t,) = R()
exec(t * 'x,y=sorted(R());a,b=R();print(min(a,b-a)*x+a*y);')

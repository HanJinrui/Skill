k = lambda : map(int, input().split())
(t,) = k()
exec(t * 'n,m=k();print(max(0,sum(k())-m));')

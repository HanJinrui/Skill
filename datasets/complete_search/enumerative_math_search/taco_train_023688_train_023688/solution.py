R = lambda : map(int, input().split())
(t,) = R()
exec(t * 'n,u,v=R();a=*R(),;d=max(abs(x-y)for x,y in zip(a,a[1:]));print(min(u,v)*(d<2)+v*(d<1));')

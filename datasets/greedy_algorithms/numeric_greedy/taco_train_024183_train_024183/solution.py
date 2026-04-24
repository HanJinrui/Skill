R = lambda : map(int, input().split())
(t,) = R()
exec(t * 'n,k=R();x,*a=sorted(R());print(sum((k-y)//x for y in a));')

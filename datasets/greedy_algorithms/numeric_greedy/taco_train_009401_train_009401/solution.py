R = lambda : [*map(int, input().split())]
exec(R()[0] * "n,m,k=R();a=R();print('YNEOS'[a.count(m:=max(a))+k*m-k>n::2]);")

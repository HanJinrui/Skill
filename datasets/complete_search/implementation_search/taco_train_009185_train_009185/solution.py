N = 100
a = (5, N, N, 2, N, N, 8, N, 0, 1)
R = lambda x=' ': map(int, input().split(x))
(t,) = R()
exec(t * "h,m=R();x,y=R(':');y+=x*m;u=v=w=q=N\nwhile h<=w+q*10or v*10+u>=m:r=f'{y//m%h:02}:{y%m:02}';y+=1;u,v,_,w,q=(a[ord(x)%10]for x in r)\nprint(r)\n")

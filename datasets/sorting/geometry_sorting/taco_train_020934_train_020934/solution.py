import math
a,b,p=list(map(float,input().split()))
ar=a*b*p/100
ans=ar*b/a
res=b-math.sqrt(ans)
print(("%.2f" % res))

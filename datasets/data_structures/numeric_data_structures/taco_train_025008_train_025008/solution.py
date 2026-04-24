import math
a,b,n = list(map(float,input().split()))
print(int(math.ceil((n-b)/(a-b))))

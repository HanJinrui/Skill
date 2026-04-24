I = lambda : map(int, input().split())
(t,) = I()
exec('n,x=I();*s,=I();print([0,2-(x in s or sum(s)==x*n)][{*s}!={x}]);' * t)

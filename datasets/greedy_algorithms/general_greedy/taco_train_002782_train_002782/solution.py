R = lambda : [*map(int, input().split())]
(t,) = R()
exec(t * 'R();a=R();b=R();print(sum(max(x-min(a),y-min(b))for x,y in zip(a,b)));')

R = lambda : {*map(int, input().split())}
(t,) = R()
exec(t * "R();s=R()&R();print(s and f'YES 1 {s.pop()}'or'NO');")

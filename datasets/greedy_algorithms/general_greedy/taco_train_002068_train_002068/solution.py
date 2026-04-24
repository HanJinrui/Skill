print(' '.join((str(k[0] + 1) for k in sorted([[i] + [int(j) for j in input().split()] for i in range(int(input()))], key=lambda x: x[1] + x[2]))))

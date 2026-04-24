p = input()
q = [input() for i in range(int(input()))]
r = [q1[1] + q2[0] for q1 in q for q2 in q]
print('Yes' if p in q + r else 'No')

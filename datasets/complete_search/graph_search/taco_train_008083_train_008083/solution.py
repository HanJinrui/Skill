input()
s1 = input()
s2 = input()
s3 = s1[0] + s1[-1] + s2[0] + s2[-1]
print((s3 == '<>v^' or s3 == '><^v') and 'YES' or 'NO')

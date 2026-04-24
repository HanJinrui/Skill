(s, k) = (input(), int(input()))
a = list(map(int, input().split()))
s += k * chr(97 + a.index(max(a)))
print(sum((a[ord(s[i]) - 97] * (i + 1) for i in range(len(s)))))

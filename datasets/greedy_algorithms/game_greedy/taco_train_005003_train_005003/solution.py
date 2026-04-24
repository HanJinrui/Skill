n = int(input())
word = input()
print(['Monocarp', 'Bicarp'][0 == sum([9 * (2 * (i < n // 2) - 1) if word[i] == '?' else (4 * (i < n // 2) - 2) * int(word[i]) for i in range(n)])])

print(*[' '.join([str(bin(i ^ i + 1).count('1')) for i in range(int(input()))]) for _ in range(int(input()))], sep='\n')

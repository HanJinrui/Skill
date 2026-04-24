a = int(input())
print(['YES', 'NO'][all((a % e for e in [4, 7, 47, 744, 477]))])

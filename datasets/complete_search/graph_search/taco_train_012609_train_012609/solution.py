import re
(r, c) = input().split()
s = '\n'.join((input().replace('.', 'D') for _ in [0] * int(r)))
print('No' if re.search('(?s)(S|W)(.{' + c + '})?(?!\\1)(S|W)', s) else 'Yes\n' + s)

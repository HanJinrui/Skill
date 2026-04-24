I = input
exec(int(I()) * "I();a=I().split();print('NYOE S'[any(x in a[i+2:]for i,x in enumerate(a))::2]);")

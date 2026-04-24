I = input
exec(int(I()) * "I();a=[f'{i} 1 {i}'for i,(x,y)in enumerate(zip(I(),I()),1)if x!=y];print(len(a)*3,*a);")

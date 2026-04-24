I = input
exec(int(I()) * 'I();b=*map(int,I().split()),;s={*range(2*len(b)+1)}-{*b};a=[]\ntry:\n for x in b:a+=x,min(s-{*range(x)});s-={*a}\nexcept:a=-1,\nprint(*a);')

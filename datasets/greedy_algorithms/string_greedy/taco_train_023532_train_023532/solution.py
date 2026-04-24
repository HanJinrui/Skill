I = input
exec(int(I()) * "n=int(I());exec('s='+('+I()'*n)[1:]);print('YNEOS'[any(s.count(x)%n for x in s)::2]);")

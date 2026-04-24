I = input
exec(int(I()) * "k=int(I().split()[1]);s=I().strip('.');r=i=1\nwhile i<len(s):i=s.rfind('*',i,i+k)+1;r+=1\nprint(r)\n")

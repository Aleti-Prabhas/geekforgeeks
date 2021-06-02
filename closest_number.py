t=int(input())
for i in range(t):
    n=int(input())
    m=int(input())
    if((n&m>0) or (n&m)<0):
        if(n%m==0):
            print("0")
        else:
            print(m*(n//m))
    else:
        print(m*(n//m))
    print(n//m)
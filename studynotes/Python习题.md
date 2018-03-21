    from random import randint
    seq=[2,3,4,5,6] 
    seq[:2]         #[2, 3]
    seq[-2:]       #[5, 6]
    seq[10:]      #[]
    seq[::-1]    #[6, 5, 4, 3, 2]

    result=[randint(1,10) for x in range(10)]
    result
    dic = {x:randint(20,30) for x in range(10)}
    dic

    x=0.5
    print(x)
    while x!=1.0:
        print(x)
        x+=0.1
        if(x>1.1):
            break

    #0.5
    #0.5
    #0.6
    #0.7
    #0.7999999999999999
    #0.8999999999999999
    #0.9999999999999999
    #1.0999999999999999

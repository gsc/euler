x = 3
y = 5
roof = 1000

def mytest2():
    print('tis is a a ttest')
    
def calcMultiplos(x,y,roof):
    m = 2
    acum = 0
    mult = []
    while True:
        #multiplos exclusivos de x
        if (m % y != 0 and x * m < roof):
            print(x*m)
            acum += (x*m)
            mult.append(x*m)
        if(x * m > roof):
            break
        else:
            m += 1

    m = 2
    while True: 
        #multiplos exclusivos de y
        if (m % x != 0 and y * m < roof):
            print(y*m)
            acum += (y*m)
            mult.append(y*m)
        if(y * m > roof):
            break
        else:
            m +=1
                            
    print('up to this point: '+str(acum))
    a = 1
    b = 1
    # True => inc a, False => inc b

    print('inc b')
    while True:
        b = a
        while True: 
            if(a * x * b * y < roof):
                if(not (a * x * b *y) in mult):
                    mult.append(a*x*b*y)
                    print (a*x*b*y)
                    acum += a * x* b*y
                b += 1
            else:
                break
        a+=1
        if(a >= (roof - y) / x):
            break
        
    #     if(a )
    # b = 1
    # print('inc a')
    # while True:
    #     if(a * x * b * y < roof):
    #         print (a*x*b*y)
    #         acum += a * x* b*y
    #         a += 1
    #     else:
    #         break
                
    return (acum +8)
        

        

    
    

    
    
    
    
    
    

# Project Euler, problem 1: Multiples of 3 and 5 (http://projecteuler.net/problem=1). 

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

x = 3
y = 5

#threshold, only multiples below 'roof' are to be summed up. 
roof = 1000

def calcMultiples(x,y,roof):
    m = 2
    acum = 0
    mult = []
    while True:
        #Multiples from x, and x only. (i.e. excluding those that are also multiples of x). 
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
        #Multiples from y, and y only (i.e. excluding those that are also multiples of x).         
        if (m % x != 0 and y * m < roof):
            print(y*m)
            acum += (y*m)
            mult.append(y*m)
        if(y * m > roof):
            break
        else:
            m +=1                            
    a = 1
    b = 1
    # True => inc a, False => inc b

    # Multiples of x and y. 
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
        
    # 8 (3+5) is added, to include the 'base' factors in the sum. 
    return (acum +8)
        

        

    
    

    
    
    
    
    
    

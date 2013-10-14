num = 600851475143

primes = [2,3,5,7,11,13,23,29,31]

def isPrime(num):

primes = [2]

for i in range(3,2000,2):
    j = 0
    while j < len(primes) and i % primes[j] !=0:
        j += 1
    if(j >= len(primes)):
        primes.append(i)


def getFactors(num):
    if(num == 1):
        return [1]
    
    for i in primes:        
        if num % i == 0:
            l = [i]
            return l + getFactors(num / i)
    print('not in primes: '+str(num))
    return [num]
            
        


    print(num)

        #print('prime '+str(i))
    #else:
    #if j == len(primes):        
    #print('not prime: ' +str(i)+' div: '+str(primes[j]))
        
        # else:
        #     print('not prime: ' +str(i)+' div: '+str(primes[j-1]))
            


       
            
            
    

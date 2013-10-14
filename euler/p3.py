# Project Euler, problem 3: Largest Prime factor (http://projecteuler.net/problem=3). 

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

num = 600851475143

#Initialization: 2 as the first prime, the rest will be computed. 
primes = [2]

# Compute the primes in the range [3,2000], skipping the even numbers (which are always multiples of 2). 
for i in range(3,2000,2):
    j = 0
    while j < len(primes) and i % primes[j] !=0:
        j += 1
    if(j >= len(primes)):
        primes.append(i)

# This function will return the factors of num.
# Note: this version works for 600851475143, because it's a product of [71, 839, 1471, 6857] (i.e all of its factors are primes in the range [3,2000], except
# for 6857, which is a prime as well. The prime calculation needs to be improved to handle numers with more than one prime factor bigger than 2000.
def getFactors(num):
    if(num == 1):
        return [1]
    
    for i in primes:        
        if num % i == 0:
            l = [i]
            return l + getFactors(num / i)
    print('not in primes: '+str(num))
    return [num]



       
            
            
    

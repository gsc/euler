// Project Euler, problem 10: Summation of primes (http://projecteuler.net/problem=10). 
// The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
// Find the sum of all the primes below two million.

import java.util.ArrayList; 
import java.util.List; 

class P10 {

    private static List<Integer> primes;
    
    public static void main(String[] args) {
	
	primes = new ArrayList<Integer>();	
	primes.add(2);	
	int numPrimes = 1; 

	// Candidate number. 
	int number = 3; 
	
	Object[] mPrimes; 
	boolean isPrime; 
	long primeSum = 2; 

	do{
	    mPrimes = primes.toArray();	    
	    
	    boolean factorFound  = false; 

	    int i = 0; 
	    do {		
		int prime = Integer.parseInt(mPrimes[i].toString());
		
		if(number % prime == 0){
		    factorFound = true; 
		    break; 
		} else
		    i++; 
	    }
	    while(!factorFound && i < primes.size());
	    
	    isPrime = (!factorFound && (i==primes.size())); 
	    
	    if(isPrime) {
		primes.add(number);
		primeSum += number; 
		//System.out.println("prime: " +number);		
		if(primes.size() % 1000 == 0)
		    System.out.println(primes.size() + " primes found"); 
	    }
	    
	    // Even numbers aren't primes (except for 2), so they're skipped. 
	    number += 2; 	    

	} while(number < 2000000); 
	//} while(number < 10);
	    //} while(number < 2); 
	System.out.println(primes.size()+" primes below 2 million"); 
	System.out.println("The sum of the primes below 2 million is : "+primeSum);
    }
}
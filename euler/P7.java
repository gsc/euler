// Project Euler, problem 7: 10001st prime (http://projecteuler.net/problem=7). 

// By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

// What is the 10 001st prime numbe
import java.util.ArrayList; 
import java.util.List; 

class P7 {
    
    private static List<Integer> primes;
    
    public static void main(String[] args) {

	primes = new ArrayList<Integer>();	
	primes.add(2);	
	int numPrimes = 1; 

	// Candidate number. 
	int number = 3; 
	
	Object[] mPrimes; 
	boolean isPrime; 

	do{
	    mPrimes = primes.toArray();	    
	    
	    isPrime = true; 
	    
	    for(int i = 0; i < mPrimes.length; i++){
		int prime = Integer.parseInt(mPrimes[i].toString());
		
		if(number % prime == 0){
		    isPrime = false; 
		    break; 
		}
	    }
	    if(isPrime) {
		primes.add(number);
		System.out.println("prime: " +number);		
	    }
	    
	    // Even numbers aren't primes (except for 2), so they're skipped. 
	    number += 2; 	    

	} while(primes.size() < 10001); 
	
	System.out.println("10001 prime: "+primes.get(primes.size()-1));
	
    }
}
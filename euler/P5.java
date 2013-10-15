// Project Euler, problem 5: smallest multiple (http://projecteuler.net/problem=5). 

// 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

// What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

class P5 {
    
    private static int[] primes = {2,3,5,7,11,13,17,19};     

    // A multiple
    public static void main(String[] args) {
	System.out.println("8%2 " + (8 % 2));

	
	// the range of divisors is defined as [1,roof]
	int roof = 20; 
	
		
	
	// The smallest number that can be divided by each of the numbers in [1, roof]
	// will be (at least) a multiple of each and every one of the primes in that range. 
			
	int mcm = 1; 
	for(int i = 0; i < P5.primes.length; i++){
	    mcm = mcm * P5.primes[i]; 
	}
	// int i = 0; 
	// do{
	//     i++;
	// }
	// while();
	    
	for(int i = 1; i < roof; i++){
	    if( (mcm % i) == 0){
		System.out.println("mcm is divisible by "+i);				
	    } else {
		int rest = mcm % i; 				
		if(isPrime(rest))
		    mcm = mcm * rest;
		else  {		    		    
		    if(rest == 4) 
			mcm  = mcm * getPrimes(rest); 
		        //mcm = mcm * 2; 				    
		    
		    if(rest == 6) 
			mcm = mcm * 6; 		       
		    
		    if(rest == 8)
			mcm = mcm * 2; 		    		    
		}		
	    }
	}
	System.out.println(mcm);
	
	// 4, divisible by 2² 
	// 6, divisible by 2 and 3. 
	// 8, divisible by 2³
	// 9, divisible by 3²
	// 10, divisible by 2 and 5
	// 12, divisible by 2² and 3
	// 14, disivible by 7 and 2
	// 15, divisible by 3 and 5
	// 16, divisible by 2⁴
	// 18, divisible by 3² and 2	    	    	    	
    }
    
    private static boolean isPrime(int num){
	for(int i = 0; i < P5.primes.length; i++)
	    if(P5.primes[i] == num)
		return true; 
	
	return false; 
    }
    
    public static int getPrimes(int rest){
	System.out.println("rest: "+rest);

	if(rest == 0)
	    return 0;

	for(int i = 0; i < P5.primes.length; i++){
	    
	    if(rest % primes[i] == 0) 
		if(rest / primes[i] == primes[i]){
		    System.out.println("prime: "+primes[i]); 
		    System.out.println("div: "+ rest / primes[i]);
		    return primes[i]; 
		} else {		    
		    int recursive = getPrimes(rest / primes[i]);
		    System.out.println("rec: "+recursive); 
		    return primes[i] * recursive; 
		}	    	
	    
	}	
	return 1; 
    }
}
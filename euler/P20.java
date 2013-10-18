// Project Euler, problem 20: Factorial digital sum (http://projecteuler.net/problem=20). 
// n! means n x (n  1) x  ...  3 x 2 x 1
// For example, 10! = 10 x  9  ...  3  x  2  x  1 = 3628800,
// and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
// Find the sum of the digits in the number 100!

import java.math.BigInteger; 

class P20 {
    
    public static void main(String[] args) {
	
	BigInteger f = factorial(100); 
	//System.out.println(f); 
	String num = String.valueOf(f); 

	long sum = 0; 
	for(int i = 0; i < num.length(); i++)
	    sum += Long.parseLong(num.substring(i,i+1)); 

	System.out.println("The sum = "+sum); 
    }

    public static BigInteger factorial(int num){
	BigInteger res = BigInteger.valueOf(1); 
	BigInteger n = BigInteger.valueOf(num); 
	
	int count = 0; 
	
	while(n.compareTo(BigInteger.valueOf(1)) == 1) {
	    
	    res = res.multiply(n); 
 	    n = n.subtract(BigInteger.valueOf(1)); 
	    // System.out.println("res: "+res); 
	    // System.out.println("n: "+n); 
	    // count++; 
	    // if(count == 4)
	    // 	break; 
	}
	return res; 
    }
}
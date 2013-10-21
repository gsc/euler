// Project Euler, problem 23: <Title> (http://projecteuler.net/problem=23). 
// A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

// A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

// As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

// Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

import java.util.ArrayList; 

class P23 {
    
    public static void main(String[] args) {
	
	long sum = 0; 
		
	ArrayList<Integer> abundant = new ArrayList<Integer>();
	//int[] abundant = new int[28123]; 
	for(int i = 12; i < 28123; i++){
	    if (getDivisorsSum(i) > i) {
		abundant.add(i); 	
		//numAbundant++; 
		System.out.println(i+" is abundant "); 
	    }    	    
	}

	for(int i = 0; i < 28124; i++){
	    
	    int j = 0; 
	    boolean found = false; 
	    
	    while(j < abundant.size() && !found){
		int elem = abundant.get(j);
		if(abundant.contains(i - elem)){
		    //System.out.println(i+ " can be expressed as the sum of "+elem+" and "+(i-elem));
		    found = true;
		}
		j++; 
	    }	 

	    if(!found) {
		System.out.println(i +" cannot be expressed as the sum of two non-abundant"); 
		sum += i; 
	    }
	}		
	System.out.println("The sum of the not-abundant is: "+sum); 
    }

    // Sum of proper divisors of num
    public static int getDivisorsSum(int num){
	int res = 0; 
	
	for(int i = 1; i < num; i++)
	    if(num % i == 0) 
		res += i; 	    
	return res; 				
    }
}
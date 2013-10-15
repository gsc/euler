// Project Euler, problem 4: Largest palindrome product (http://projecteuler.net/problem=4). 

// A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.
// Find the largest palindrome made from the product of two 3-digit numbers.

class P4 {
    
    public static Boolean isPalindrome(int num){
	String strNum = String.valueOf(num);
	
	int i = 0; 
	
	while(strNum.charAt(i) == strNum.charAt(strNum.length() - i -1) && i < strNum.length() / 2){	    	    
	    i++; 
	}
	return (i == strNum.length() / 2);
    }

    
    public static void main(String[] args) {
	boolean found = false; 
	int biggest = 0; 
	// Explore only the "upper" half of the range [500, 999]. 
	// The biggest palindrome is more likely to be the product of two values in this range. 
	for(int i = 999; i > 500; i--){
	    for(int j = i; j > 500; j--){
		if(isPalindrome(i * j) && i*j > biggest){
		    biggest = i * j; 			
		    System.out.println("i: "+String.valueOf(i)+" j: "+String.valueOf(j));
		    System.out.println(i*j);
		}
	    }
	}
    }    
}
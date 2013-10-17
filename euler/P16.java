// Project Euler, problem 16: Power digit sum (http://projecteuler.net/problem=16). 
// 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
// What is the sum of the digits of the number 21000?

import java.lang.Math; 
import java.math.BigInteger;

class P16 {
    
    public static void main(String[] args) {
	//Long isn't enough precise for such a big value. 
	//Double value is expressed in scientific notation. 
	String strNum = BigInteger.valueOf(2).pow(1000).toString();				
	long sum = 0; 

	for(int i = 0; i < strNum.length(); i++){	    
	    sum += Integer.parseInt(strNum.substring(i,i+1));
	}
	System.out.println("Sum: "+sum);		    	
    }
}
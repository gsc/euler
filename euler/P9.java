// Project Euler, problem 9: Special pythagorean triplet (http://projecteuler.net/problem=9). 

// A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

// a2 + b2 = c2
// For example, 32 + 42 = 9 + 16 = 25 = 52.

// There exists exactly one Pythagorean triplet for which a + b + c = 1000.
// Find the product abc.

class P9 {
    
    public static void main(String[] args) {
	
	int res = search();
	if(res == -1 )
	    System.out.println("No solution was found");
	else
	    System.out.println("Result: "+res);
	
    }

    private static int search(){
	for(int a = 1; a <= 1000; a ++)
	    for(int b = 1; b <= 1000; b++)
		for(int c = 1; c <= 1000; c++){
		    if(isPythagoreanTriplet(a,b,c) && verifiesEquationB(a,b,c))
			return a * b * c;
		}
	return -1; 	
    }
    
    // a^2 + b^2 = c^2
    private static boolean isPythagoreanTriplet(int a, int b, int c){
	return (a*a + b*b == c*c);
    }
    
    // a + b + c = 1000
    private static boolean verifiesEquationB(int a, int b, int c){
	return (a  + b + c == 1000);
    }
}
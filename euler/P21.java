// Project Euler, problem 21: Amicable numbers (http://projecteuler.net/problem=21). 
// Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
// If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair and each of a and b are called amicable numbers.

// For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
// d(a) == b && d(b) == a
// sum[a] == sum[sum[a]]

// Evaluate the sum of all the amicable numbers under 10000.

class P21 {
    
    public static void main(String[] args) {
	
	int roof = 10000; 
	
	int sum[] = new int[roof]; 
	
	//Compute the sum of proper divisors for every number under 10000. 
	for(int i = 0; i < roof; i++)
	    sum[i] = d(i); 	    	    	
	
	int res = 0; 
	
	for(int a = 0; a < roof; a++){
	    if(sum[a] < roof){
		int b = sum[a]; 
		if(b != a && sum[b] == a) {
		    System.out.println(a+ " and "+ b+" are amicable "); 
		    System.out.println("sum[a] : "+sum[a]); 
		    System.out.println("sum[b] : "+sum[b]); 
		    res += (b + a);
		}
	    }
	}	
	//While looping over the numbers in [0,roof], each pair a,b will be recognized as amicable two times (when i = a, and when i = b)	
	//Divide by two to count them only once.
	System.out.println("Sum amicable numbers: "+(res / 2)); 
    }

    // Sum of proper divisors of n. 
    public static int d(int num){
	
	int res = 0; 
	
	for(int i = 1; i < num; i++)
	    if(num % i == 0) 
		res += i; 	    
	return res; 			
    }
}
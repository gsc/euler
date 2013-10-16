// Project Euler, problem 14: Longest Collatz sequence (http://projecteuler.net/problem=14). 
// The following iterative sequence is defined for the set of positive integers:
// n  -> n/2 (n is even)
// n  -> 3n + 1 (n is odd)

// Using the rule above and starting with 13, we generate the following sequence:

// 13  40  20  10  5  16  8  4  2  1
// It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

// Which starting number, under one million, produces the longest chain?
// NOTE: Once the chain starts the terms are allowed to go above one million.


class P14 {
    
    public static void main(String[] args) {
	long startTime = System.nanoTime();

	long n = 837799; 
	System.out.print(n); 
	while(n > 1){
	    n = collatzSequence(n);
	    System.out.print(" -> "+n );
	}
	System.out.println(); 
	System.out.println("numSteps (837799): " +numSteps(837799)); 
	 
	int maxSteps = 0; 
	int steps; 
	int longest  = 0; 

	for(int i = 2; i < 1000000; i++){
	    steps = numSteps(i); 
	    //System.out.println("starting number: "+i+" numSteps: "+steps);
	    if(steps >= maxSteps) {

		//System.out.println("best: "+longest+" numSteps: "+maxSteps);
		maxSteps = steps; 
		longest = i; 
	    }	    
	    //System.out.println(i+" steps:"+numSteps(i));
	}

	// System.out.println("999108 steps:"+numSteps(999108));
	System.out.println("best: "+longest+" numSteps: "+maxSteps);

	long endTime = System.nanoTime();	
	long duration = endTime - startTime;
	System.out.println("duration: "+(duration / 1000000)+ " miliseconds"); 
    }

    private static long collatzSequence(long n){	
	if(n % 2 == 0){
	    // Even
	    return n / 2; 
	} else {
	    return 3 * n + 1;
	}	
    }
    
    private static int numSteps(long n){

	int steps = 1; 
	while(n > 1) {
	    n = collatzSequence(n); 
	    steps++; 
	}; 
	return steps; 
    }
    
}
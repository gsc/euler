// Project Euler, problem 61: Maximum path sum II (http://projecteuler.net/problem=61). 

// By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
// That is, 3 + 7 + 4 + 9 = 23.
// Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.
// NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)

import java.util.ArrayList; 
import java.io.IOException;
import java.io.FileReader; 
import java.io.BufferedReader; 


class P67 {

    private static final String FILE_NAME = "triangle.txt";        

    private static final int NUM_ROWS = 100;  
    private static int[][] pyramid = new int[NUM_ROWS][NUM_ROWS];         
    private static long[][] cache = new long[NUM_ROWS][NUM_ROWS];     
        
    private static boolean verbose = false; 
    
    //Caching strategy: compute only once the cost from one point to the target. 
    //It seems to work fine even for the larger triangle (100 rows), without pruning. 
    
    public static void main(String[] args) {
	
	initializeCache();
	
	try{
	    readFile(FILE_NAME);
	} catch (IOException ex ){
	    System.out.println("Something went wrong reading the file! "); 
	    return; 
	}
	
	int x = 0; 
	int y = 0; 
		
	long cost = pyramid[x][y]; 
	
	ArrayList<Integer> route = new ArrayList<Integer>();
	
	long best = bestPath(x,y);
	System.out.println("The best path from the top to the bottom has a value of :"+best); 		
    }
    
    /**
     * Load the text file into the "pyramid" attribute. 
     **/
    private static void readFile(String aFileName) throws IOException {
	
	BufferedReader reader = null; 
	
	int numRow = 0; 
	try{
	    
	    String line = null;
	    reader =  new BufferedReader(new FileReader(aFileName)); 
	    while ((line = reader.readLine()) != null) {
		int[] row = readLine(line);
		pyramid[numRow]  = row; 		    
		numRow++; 
	    }	    
	}  finally {
	    if(reader != null)
		reader.close(); 	    
	}
    }

    /**
     * Transforms the read line (String) into an array of integers. 
     **/
    private static int[] readLine(String line){
	String[] splitLine =  line.split(" ");
	
	int res[] = new int[splitLine.length]; 
	
	for(int i = 0; i < splitLine.length; i++){
	    res[i]  = Integer.parseInt(splitLine[i]); 
	}
	
	return  res; 
    }
    
    private static void initializeCache(){
	int x = 0; 
	int y = 0; 
	
	do {
	    for(int j = 0; j < x+1; j++)
		cache[x][j] = -1; 	    

	    x++; 	    	    

	} while(x < NUM_ROWS); 
    }

    /**
     * Returns the value of the best path from (x,y) to the bottom of the triangle.
     **/
    private static long bestPath(int x, int y){
	if(x == pyramid.length - 1) {
	    if(verbose)
		System.out.println("Terminal case ("+x+", "+y+") -> "+pyramid[x][y]);
	    
	    return pyramid[x][y]; 
	}

	
	long rightCost = -1;
	long leftCost  = -1;        

	if(validState(x+1, y+1)){	    
	    if(cache[x+1][y+1] != -1) 
		rightCost =  cache[x+1][y+1]; 
	    else {
		rightCost = bestPath(x+1, y+1);
		cache[x+1][y+1] = rightCost; 
	    }
	}
	
	if(validState(x+1, y)){	    
	    if(cache[x+1][y] != -1) 
		leftCost =  cache[x+1][y];
	    else  {
		leftCost = bestPath(x+1, y);
		cache[x+1][y] = leftCost; 
	    }	
	}
	
	if(verbose) {
	    if(leftCost > rightCost)
		System.out.println("choosing left on ("+x+","+y+") ("+(x+1)+","+y+") "+pyramid[x][y]+" "+leftCost); 
	    else
		System.out.println("choosing right on ("+x+","+y+") ("+(x+1)+","+(y+1)+") "+pyramid[x][y]+" "+rightCost); 
	}
	
	return pyramid[x][y] + (leftCost > rightCost ? leftCost : rightCost); 	
    }
    
    /**
     * Verifies whether a set of coordinates (x,y) corresponds to a valid position in the triangle. 
     **/
    private static boolean validState(int x,int y){
	return (x < pyramid.length && y < pyramid[pyramid.length-1].length); 
    }
}
// Project Euler, problem 15: Lattice paths (http://projecteuler.net/problem=15). 

// Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
// How many such routes are there through a 20x20 grid?

class P15 {
    
    private static final int dim = 20; 
    
    private static int dest_x  = dim; 
    private static int dest_y  = dim; 

    // to cache the number of steps from one point to the destination. 
    private static long[][] cache = new long[dim+1][dim+1];
    
    public static void main(String[] args) {
	int x = 0; 
	int y = 0; 
	
	for(int i = 0; i < dim+1; i++){
	    for(int j = 0; j < dim+1; j++){
		cache[i][j] = -1; 
	    }
	}
			
	System.out.println("Number of paths: "+numPaths(x,y)); 
    }
    

    /**
     * Returns the number of steps from state to the destination. 
     **/
    private static long numPaths(int x, int y) {	
	long nPaths= 0; 

	if(x == dest_x  && y == dest_y){
	    return 1; 
	}
	
	
	if(validState(x,y+1)){	 
	    if(cache[x][y+1] != -1) { 
		nPaths += cache[x][y+1];
	    } else {
		long res = numPaths(x, y+1);
		nPaths += res;
		cache[x][y+1] = res; 
	    }
	}
	
	if(validState(x+1,y)) {
	    if(cache[x+1][y] != -1) { 
		nPaths += cache[x+1][y];
	    } else {
		long res = numPaths(x+1, y);
		nPaths += res;
		cache[x+1][y] = res; 
	    }		
	}
		
	return nPaths; 
    }
    
    private static boolean validState(int x, int y){
	return (x <= dest_x && y <= dest_y); 
    }
}
// Project Euler, problem 18: Maximum path sum I (http://projecteuler.net/problem=18). 

// By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

// That is, 3 + 7 + 4 + 9 = 23.

// Find the maximum total from top to bottom of the triangle below:

// NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)

import java.util.ArrayList; 

class P18 {
    private static int[][] pyramid = {{75}, {95,64},{17,47,82},{18,35,87,10},{20,4,82,47,65},{19,1,23,75,3,34}, 
    		       {88,2,77,73,7,63,67},{99,65,4,28,6,16,70,92},{41,41,26,56,83,40,80,70,33},
    		       {41,48,72,33,47,32,37,16,94,29},{53,71,44,65,25,43,91,52,97,51,14},
    		       {70,11,33,28,77,73,17,78,39,68,17,57},{91,71,52,38,17,14,91,43,58,50,27,29,48},
    		       {63,66,4,68,89,53,67,30,73,16,69,87,40,31},{4,62,98,27,23,9,70,98,73,93,38,53,60,4,23}};


    private static int[][] cache = {{-1}, {-1,-1},{-1,-1,-1},{-1,-1,-1,-1},{-1,-1,-1,-1,-1},{-1,-1,-1,-1,-1,-1}, 
    				    {-1,-1,-1,-1,-1,-1,-1},{-1,-1,-1,-1,-1,-1,-1,-1},{-1,-1,-1,-1,-1,-1,-1,-1,-1},
    				    {-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},{-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
    				    {-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},{-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
    				    {-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},{-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1}};

    // private static int[][] pyramid = {{3},{7,4},{2,4,6},{8,5,9,3}};
    // private static int[][] cache = {{-1},{-1,-1},{-1,-1,-1},{-1,-1,-1,-1}};
        
    public static void main(String[] args) {
	//Greedy implementation. 
	int x = 0; 
	int y = 0; 
		
	int cost = pyramid[x][y]; 
	
	ArrayList<Integer> route = new ArrayList<Integer>();
	
	int best = bestPath(x,y);
	System.out.println(best); 
	
	// do{	
	//     if(pyramid[x][y] <= pyramid[x][y+1])	       
	// 	y = y+1; 
	//     // else, go through the left child (y' == y). 
	//     cost += pyramid[x][y]; 
	//     route.add(pyramid[x][y]);
	//     x += 1; 
	    
	// } while(x  < pyramid.length);
	
	// System.out.println("route cost: "+cost); 
	// for(Integer i : route){
	//     System.out.println(i); 
	// }
	
    }

    private static int bestPath(int x, int y){
	//System.out.println("x: "+x+" y: "+y); 
	if(x == pyramid.length - 1) {
	    System.out.println("Terminal case ("+x+", "+y+") -> "+pyramid[x][y]);
	    return pyramid[x][y]; 
	}

	
	int rightCost = -1;
	int leftCost  = -1;        

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
	if(x == 14 && y == 0)
	    System.out.println("Left: " +leftCost +" right: "+rightCost); 
	
	if(leftCost > rightCost)
	    System.out.println("choosing left on ("+x+","+y+") ("+(x+1)+","+y+") "+pyramid[x][y]+" "+leftCost); 
	else
	    System.out.println("choosing right on ("+x+","+y+") ("+(x+1)+","+(y+1)+") "+pyramid[x][y]+" "+rightCost); 
	
	return pyramid[x][y] + (leftCost > rightCost ? leftCost : rightCost); 	
    }
    
    private static boolean validState(int x,int y){
	return (x < pyramid.length && y < pyramid[pyramid.length-1].length); 
    }
//      [0]
//    [0][1]
//   [0][1][2]
//  [0][1][2][3]
// [0][1][2][3][4]

}
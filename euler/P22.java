// Project Euler, problem 22: <Title> (http://projecteuler.net/problem=22). 
// Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

// For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938  53 = 49714.

// What is the total of all the name scores in the file?

import java.io.IOException;
import java.io.FileReader; 
import java.io.BufferedReader; 
import java.util.Arrays; 

class P22 {
    
    private static final String FILE_NAME = "names.txt";
    
    private static String[] readFile(String fileName) throws IOException{
	BufferedReader reader = null; 
	
	String line = null; 
	reader = new BufferedReader(new FileReader(fileName)); 
	line = reader.readLine(); 	
	reader.close(); 

	String[] names  = line.split(","); 
	
	// remove the "" sorrounding the name. 
	for(int i =0; i < names.length; i++)
	    names[i] = names[i].substring(1,names[i].length()-1); 
	
	return names; 
    }
    
    public static int getValue(String name){
	
	char[] letters = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};
	
	int value = 0; 
	
	for(int i = 0; i < name.length(); i++)
	    value += (int)(name.charAt(i) - 'A' +1); 

	return value; 
    }

    
    public static void main(String[] args) {
	
	String[] names = null; 
	
	try{
	    names = readFile(FILE_NAME); 
	    
	} catch(IOException ex) {
	    System.out.println("Cannot read file!" ); 
	}
	
	Arrays.sort(names); 

	long sum = 0; 
	
	for(int i = 0; i < names.length; i++){	    
	    int nameValue = getValue(names[i]);

	    System.out.println("Name ["+i+"]: "+names[i]+" value: "+nameValue+" score: "+ ((i+1)*nameValue)); 
	    sum+= (i+1) * nameValue; 
	    System.out.println(sum); 
	}
	
	
	System.out.println("Scores sum "+sum); 		
    }
    
}


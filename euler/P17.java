// Project Euler, problem 17: Number letter counts (http://projecteuler.net/problem=17). 

// If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
// If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
// NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

class P17 {
    
    public static void main(String[] args) {

	String[] numbers = writeNumbers();
	long totalCount = 0; 
	for(int i = 1; i < 1000; i++){
	    int count = letterCount(numbers[i]);
	    //System.out.println(i+" -> "+numbers[i]+" "+count); 
	    totalCount += count;
	}
	totalCount += letterCount("one thousand"); 
	System.out.println("Number of letters: "+totalCount); 
    }

    private static String[] writeNumbers() {

	String[] units  = {"one", "two", "three", "four", "five","six", "seven", "eight", "nine"}; 
	String[] teens = {"ten","eleven", "twelve", "thirteen", "fourteen", "fifteen","sixteen", "seventeen", "eighteen", "nineteen"};
	String[] tys = {"twenty", "thirty", "forty","fifty","sixty","seventy", "eighty", "ninety"}; 
	
	String[] numbers = new String[1000]; 
	for(int i = 1; i < 1000; i++){
	    
	    int unit = i % 10; 
	    int tens = (i % 100) / 10;
	    int hundred = i / 100; 
	    if(hundred > 0) {
		if(tens == 0 && unit == 0) {
		    numbers[i] = units[hundred-1]+" hundred"; 
		    continue; 
		} else
		    numbers[i] = units[hundred-1]+" hundred and "; 
	    } else 
		numbers[i] = ""; 

	    if(tens == 1) {
		numbers[i] += teens[unit]; 
		continue; 
	    }
	    
	    if(tens > 1)
		numbers[i] += tys[tens - 2] + (unit > 0 ? "-" : "") ; 
	    
	    if(unit > 0)
		numbers[i] += units[unit-1]; 			    	
	}
	return numbers; 
    }


    private static int letterCount(String number){
	int count = 0; 
	for(int i = 0; i < number.length(); i++){
	    char letter = number.charAt(i);
	    if(letter != ' ' && letter != '-')
		count ++;
	}

	return count; 
    }


}
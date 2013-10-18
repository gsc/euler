// Project Euler, problem 19: Counting Sundays (http://projecteuler.net/problem=19). 
// You are given the following information, but you may prefer to do some research for yourself.

// 1 Jan 1900 was a Monday.
// Thirty days has September,
// April, June and November.
// All the rest have thirty-one,
// Saving February alone,
// Which has twenty-eight, rain or shine.
// And on leap years, twenty-nine.
// A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
// How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

import java.util.Calendar; 
import java.util.GregorianCalendar; 

class P19 {
    
    // Solution: use the class Calendar. 

    public static void main(String[] args) {

	Calendar c = new GregorianCalendar(); 
	c.set(1901, 1, 1); 

	int count = 0; 
	while(c.get(Calendar.YEAR) < 2001) {
	    if(c.get(Calendar.DAY_OF_WEEK) == Calendar.SUNDAY)
		count++; 	    	    
	    
	    c.add(Calendar.MONTH, 1); 	    
	} 

	System.out.println("Number of mondays :"+count); 		
    }    
}
import static org.junit.Assert.assertEquals;

import org.junit.Test;
import org.junit.Ignore;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;
import java.lang.reflect.Method; 

import static org.junit.Assert.fail;

/**
 * Tests for {@link P17}.
 *
 * @author guillelmo@gmail.com (gsc)
 */
@RunWith(JUnit4.class)
public class P17Test {
    @Test
    public void testLetterCount() {
	try{	
	    Method method = P17.class.getDeclaredMethod("letterCount", new Class[] {String.class});
	    method.setAccessible(true);
	    
	    
	    int res1 = (Integer)method.invoke("letterCount", new Object[]{"three hundred and forty-two"});	    	    
	    int res2 = (Integer)method.invoke("letterCount", new Object[]{"one hundred and fifteen"});	    	    
	    
	    assertEquals(23,res1); 
	    assertEquals(20,res2); 
	    
	    int numLetters = 0; 	
	    String[] numbers = {"one", "two", "three", "four", "five"}; 

	    for(int i = 0; i < 5; i++){		
		numLetters += (Integer)method.invoke("letterCount", new Object[]{numbers[i]});	    	    
	    }
	    assertEquals(19, numLetters); 
	} catch(Exception ex) {
	    fail("Exception");
	}
    }
    
    @Test 
    public void testWriteNumbers(){
	try{
	    Method method = P17.class.getDeclaredMethod("writeNumbers");
	    method.setAccessible(true);
	    
	    
	    String[] numbers = (String[])method.invoke("writeNumbers");	    	    
	    
	    assertEquals(numbers[1],"one"); 

	    assertEquals(numbers[10],"ten"); 
	    assertEquals(numbers[20],"twenty"); 
	    System.out.println(numbers[21]); 
	    assertEquals(numbers[21],"twenty-one"); 

	    assertEquals(numbers[100],"one hundred"); 
	    assertEquals(numbers[101],"one hundred and one"); 
	    assertEquals(numbers[110],"one hundred and ten"); 
	    assertEquals(numbers[120],"one hundred and twenty"); 
	    assertEquals(numbers[121],"one hundred and twenty-one"); 
	    
	    System.out.println(numbers[342]); 
	    
	    assertEquals(numbers[342],"three hundred and forty-two"); 
	    assertEquals(numbers[115],"one hundred and fifteen"); 
	    
	    
	} catch(Exception ex) {
	    fail("Exception");
	}	
    }
    


    // @Test
    // @Ignore
    // public void thisIsIgnored() {
    // }
}
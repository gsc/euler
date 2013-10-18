import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.fail;

import org.junit.Test;
import org.junit.Ignore;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;

import java.lang.reflect.Method; 
import java.lang.reflect.InvocationTargetException; 

/**
 * Tests for {@link P67}.
 *
 * @author guillelmo@gmail.com (gsc)
 */
@RunWith(JUnit4.class)
public class P67Test {
    
    @Test
    public void testReadLine() {
	String[] input = {"51", 
		"73 41", 
		"52 40 09", 
			  "23 33 44 81 80 92 93 75 94 88 23 61 39 76 22 03 28 94 32 06 49 65 41 34 18 23 08 47 62 60 03 63 33 13 80 52 31 54 73 43 70 26 16 69 57 87 83 31 03 93 70 81 47 95 77 44 29 68 39 51 56 59 63 07 25 70 07 77 43 53 64 03 94 42 95 39 18 01 66 21 16 97 20 50 90 16 70 10 95 69 29 06 25 61 41 26 15 59 63 35"};
	
	int[][] output = {
	    {51}, 
	    {73,41},
	    {52,40,9},
	    {23,33,44,81,80,92,93,75,94,88,23,61,39,76,22,3,28,94,32,6,49,65,41,34,18,23,8,47,62,60,3,63,33,13,80,52,31,54,73,43,70,26,16,69,57,87,83,31,3,93,70,81,47,95,77,44,29,68,39,51,56,59,63,7,25,70,7,77,43,53,64,3,94,42,95,39,18,1,66,21,16,97,20,50,90,16,70,10,95,69,29,6,25,61,41,26,15,59,63,35}	    
	};
	
	try {
	    Method method = P67.class.getDeclaredMethod("readLine", new Class[] {String.class});
	    method.setAccessible(true);
	    
	    for(int i = 0; i < input.length; i++){
		int[] res = (int[])method.invoke("readLine", new Object[]{input[i]});	    	    
		assertArrayEquals(output[i], res); 
	    }
	    
	} catch (Exception ex){
	    if(ex instanceof NoSuchMethodException | ex instanceof IllegalAccessException | ex instanceof InvocationTargetException){
		fail("Tested method doesn't exist");
	    } else {
		fail("Something went wrong! "); 
	    }	    
	} 	
    }

    // @Test
    // @Ignore
    // public void thisIsIgnored() {
    // }
}
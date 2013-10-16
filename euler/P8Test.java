//Empty Template for Unit test of Project Euler Problems. 

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.fail;

import org.junit.Test;
import org.junit.Ignore;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;
import java.lang.reflect.Method; 
//import junitx.util.PrivateAccessor;


/**
 * Tests for {@link PN}.
 *
 * @author guillelmo@gmail.com (gsc)
 */
@RunWith(JUnit4.class)
public class P8Test {

    @Test
    public void testGetSplits() {
	try{
	    Method method = P8.class.getDeclaredMethod("getSplits", new Class[] {String.class,int.class});
	    method.setAccessible(true);

	    int[][] res = (int[][])method.invoke("getSplits", new Object[]{"123456",2});	    	    
	    assertEquals(5,res.length);
	    
	    assertEquals(1,res[0][0]);
	    assertEquals(2,res[0][1]);
	    
	    assertEquals(2,res[1][0]);
	    
	    assertEquals(5,res[4][0]);
	    assertEquals(6,res[4][1]);
	    
	    res = (int[][])method.invoke("getSplits", new Object[]{"123456",3});
	    
	    assertEquals(4,res.length);
	    
	    assertEquals(1,res[0][0]);
	    assertEquals(3,res[0][2]);
	    
	    assertEquals(2,res[1][0]);
	    assertEquals(4,res[1][2]);
	    
	    assertEquals(4,res[3][0]);
	    assertEquals(6,res[3][2]);
	
	} catch(Exception ex) {
	    fail("Exception");
	}
    }

	
    
    // @Test
    // @Ignore
    // public void thisIsIgnored() {
    // }
}
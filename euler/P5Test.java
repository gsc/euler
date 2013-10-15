//Empty Template for Unit test of Project Euler Problems. 

import static org.junit.Assert.assertEquals;

import org.junit.Test;
import org.junit.Ignore;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;

/**
 * Tests for {@link P5}.
 *
 * @author guillelmo@gmail.com (gsc)
 */
@RunWith(JUnit4.class)
public class P5Test {

    @Test
   public void testGetPrimes() {
	assertEquals(4, P5.getPrimes(8));
	assertEquals(6, P5.getPrimes(6));	
	assertEquals(2, P5.getPrimes(4));	
	assertEquals(2, P5.getPrimes(8));	
    }

    // @Test
    // @Ignore
    // public void thisIsIgnored() {
    // }
}
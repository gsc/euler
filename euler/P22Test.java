//Empty Template for Unit test of Project Euler Problems. 

import static org.junit.Assert.assertEquals;

import org.junit.Test;
import org.junit.Ignore;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;

/**
 * Tests for {@link PN}.
 *
 * @author guillelmo@gmail.com (gsc)
 */
@RunWith(JUnit4.class)
public class P22Test {

    @Test
    public void testGetValue() {
	assertEquals(53, P22.getValue("COLIN")); 
    }

    // @Test
    // @Ignore
    // public void thisIsIgnored() {
    // }
}
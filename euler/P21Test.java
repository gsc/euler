import static org.junit.Assert.assertEquals;

import org.junit.Test;
import org.junit.Ignore;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;

/**
 * Tests for {@link 21}.
 *
 * @author guillelmo@gmail.com (gsc)
 */
@RunWith(JUnit4.class)
public class P21Test {
    
    @Test
    public void testD() {
	assertEquals(284, P21.d(220));
	assertEquals(220, P21.d(284));
    }

    // @Test
    // @Ignore
    // public void thisIsIgnored() {
    // }
}
import static org.junit.Assert.assertEquals;

import org.junit.Test;
import org.junit.Ignore;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;

/**
 * Tests for {@link P4}.
 *
 * @author guillelmo@gmail.com (gsc)
 */
@RunWith(JUnit4.class)
public class P4Test {

    @Test
    public void testIsPalindrome() {
	assertEquals(P4.isPalindrome(14), false);	
	assertEquals(P4.isPalindrome(11), true);	
	assertEquals(P4.isPalindrome(99), true);	
	
	// Possible palindromes of three digits, in the form: aba, aaa
	assertEquals(P4.isPalindrome(121), true);		
	assertEquals(P4.isPalindrome(222), true);			

	assertEquals(P4.isPalindrome(123), false);		

	// Possible palindromes of four digits, in the form: abba, aaaa
	
	assertEquals(P4.isPalindrome(3333), true);		
	assertEquals(P4.isPalindrome(4114), true);		
	
	//No Palindromes: abca, abbc, abab
	assertEquals(P4.isPalindrome(1231), false);		
	assertEquals(P4.isPalindrome(3224), false);		
	assertEquals(P4.isPalindrome(3232), false);		

	// Possible palindromes of five digits, in the form: abcba, aaaaa, aabaa
	assertEquals(P4.isPalindrome(12321), true);		
	assertEquals(P4.isPalindrome(32123), true);		
	assertEquals(P4.isPalindrome(11311), true);		
	assertEquals(P4.isPalindrome(11111), true);		

	// Possible palindromes of six digits, in the form: abccba, aaaaaa, aabbaa
	assertEquals(P4.isPalindrome(123321), true);		
	assertEquals(P4.isPalindrome(321123), true);				
	assertEquals(P4.isPalindrome(332233), true);				
    }

    // @Test
    // @Ignore
    // public void thisIsIgnored() {
    // }
}
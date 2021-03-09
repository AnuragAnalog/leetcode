class Solution
{
public:
    int removePalindromeSub(string s)
    {
        if (s.size() == 0)
        {
            return 0;
        }
        
        if (checkPalindrome(s))
        {
            return 1;
        }
        
        return 2;
    }
    
    bool checkPalindrome(string s)
    {

        int n = s.length(); 

        for ( int i = 0; i <= n/2; i++ ) 
        {
            if ( s[i] != s[n-1-i] )
                return false;
        }

        return true;
    }
};
class Solution {
public:
    int romanToInt(string s)
    {
        int     i, num = 0;
        map <char, int> encoding;
        
        encoding['I'] = 1;
        encoding['V'] = 5;
        encoding['X'] = 10;
        encoding['L'] = 50;
        encoding['C'] = 100;
        encoding['D'] = 500;
        encoding['M'] = 1000;

        for (i = 0; i < s.size(); i++)
        {
            if (encoding[s[i]] < encoding[s[i+1]])
            {
                num = num - encoding[s[i]];
            }
            else
            {
                num = num + encoding[s[i]];
            }
        }
        
        return num;
    }
};

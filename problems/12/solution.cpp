class Solution
{
public:
    string intToRoman(int num)
    {
        map <int, string>    encoding;
        int        i = 0, j, q;
        vector <int>    roman;
        string roman_s;
        
        encoding[1] = 'I';
        encoding[2] = 'V';
        encoding[3] = 'X';
        encoding[4] = 'L';
        encoding[5] = 'C';
        encoding[6] = 'D';
        encoding[7] = 'M';

        if (num%1000 > 0)
        {
            q = num / 1000;
            
            for (j = 0; j < q; j++)
            {
                roman.push_back(7);
                i = i + 1;
            }
        }
        else
        {
            q = num / 1000;
            
            for (j = 0; j < q; j++)
            {
                roman.push_back(7);
                i = i + 1;
            }
        }
        num = num - q * 1000;
        
        if (num/100 == 9)
        {
            roman.push_back(5);
            roman.push_back(7);
            i = i + 2;
        }
        else if (num/100 >= 4 && num/100 <= 8)
        {
            if (num/100 == 4)
            {
                roman.push_back(5);
                roman.push_back(6);
                i = i + 2;
            }
            else
            {
                roman.push_back(6);
                i = i + 1;
                for (j = 0; j < num/100-5; j++)
                {
                    roman.push_back(5);
                    i = i + 1;
                }
            }
        }
        else
        {
            for (j = 0; j < num/100; j++)
            {
                roman.push_back(5);
                i = i + 1;
            }
        }
        
        num = num - (num/100)*100;
        
        if (num/10 == 9)
        {
            roman.push_back(3);
            roman.push_back(5);
            i = i + 2;
        }
        else if (num/10 >= 4 && num/10 <= 8)
        {
            if (num/10 == 4)
            {
                roman.push_back(3);
                roman.push_back(4);
                i = i + 2;
            }
            else
            {
                roman.push_back(4);
                i = i + 1;
                for (j = 0; j < num/10-5; j++)
                {
                    roman.push_back(3);
                    i = i + 1;
                }
            }
        }
        else
        {
            for (j = 0; j < num/10; j++)
            {
                roman.push_back(3);
                i = i + 1;
            }
        }
        
        num = num - (num/10)*10;
        
        if (num == 9)
        {
            roman.push_back(1);
            roman.push_back(3);
            i = i + 2;
        }
        else if (num >= 4 && num <= 8)
        {
            if (num == 4)
            {
                roman.push_back(1);
                roman.push_back(2);
                i = i + 2;
            }
            else
            {
                roman.push_back(2);
                i = i + 1;
                for (j = 0; j < num-5; j++)
                {
                    roman.push_back(1);
                    i = i + 1;
                }
            }
        }
        else
        {
            for (j = 0; j < num; j++)
            {
                roman.push_back(1);
                i = i + 1;
            }
        }
        
        for (auto c: roman)
        {
            roman_s += encoding[c];
        }
        
        return roman_s;
    }
};

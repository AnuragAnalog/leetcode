class Solution
{
public:
    int minimumLengthEncoding(vector<string>& words)
    {
        int                       i, len = 0;
        set <string>              unique;
        
        for (string s1 : words)
        {
            unique.insert(s1);
        }

        for (string s1 : words)
        {
            for (i = 1; i < s1.size(); i++)
            {
                unique.erase(s1.substr(i, s1.size()-i));
            }
        }
        
        for (auto elem: unique)
        {
            len += elem.size() + 1;
        }
        
        return len;
    }
};
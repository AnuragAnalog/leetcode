class Solution
{
public:
    int distributeCandies(vector<int>& candyType)
    {
        int        i, n = candyType.size();
        unordered_set <int> candies;
        
        for (i = 0; i < candyType.size(); i++)
        {
            candies.insert(candyType[i]);
        }
        
        if (candies.size() >= n/2)
        {
            return n/2;
        }
        else
        {
            return candies.size();
        }
    }
};
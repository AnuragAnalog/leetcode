class Solution
{
public:
    int missingNumber(vector<int>& nums)
    {
        int        i, n, sum;
        
        n = nums.size();
        sum = (n * (n + 1)) / 2;
        
        for (i = 0; i < n; i++)
        {
            sum = sum - nums[i];
        }
        
        return sum;
    }
};
class Solution
{
public:
    vector<int> twoSum(vector<int>& nums, int target)
    {
        int        i, j;
        vector <int> sol;
        
        for (i = 0; i < nums.size(); i++)
        {
            for (j = i+1; j < nums.size(); j++)
            {
                if (nums[i] + nums[j] == target)
                {
                    sol.push_back(i);
                    sol.push_back(j);
                    
                    return sol;
                }
            }
        }
        
        return sol;
    }
};

class Solution
{
public:
    vector<int> findErrorNums(vector<int>& nums)
    {
        int i;
        int n = 0;
        vector <int> arr;
        unordered_set <int> unique;
        
        for (i = 0; i < nums.size(); i++)
        {
            if (unique.find(nums[i]) != unique.end())
            {
                arr.push_back(nums[i]);
            }
            else
            {
                if (n < nums[i])
                {
                    n = nums.size();
                }
                unique.insert(nums[i]);
            }
        }

        for (i = 1; i < n+1; i++)
        {
            if (unique.find(i) == unique.end())
            {
                arr.push_back(i);
            }
        }
        return arr;
    }
};
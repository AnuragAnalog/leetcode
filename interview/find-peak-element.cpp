class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int i, peak = -1;
        
        if (nums.size() == 1)
        {
            return 0;
        }
        
        for (i = 0; i < nums.size(); i++)
        {
            if (i == 0)
            {
                if (nums[i] > nums[i+1])
                {
                    peak = i;
                    break;
                }
            }
            else if (i == nums.size()-1)
            {
                if (nums[i-1] < nums[i])
                {
                    peak = i;
                    break;
                }
            }
            else
            {
                if (nums[i] > nums[i+1] && nums[i-1] < nums[i])
                {
                    peak = i;
                    break;
                }
            }
        }
        
        return peak;
    }
};
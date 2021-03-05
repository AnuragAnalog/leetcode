/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution
{
public:
    vector<double> averageOfLevels(TreeNode* root)
    {
        int                   i, level = 0, maxLevel = 0;
        vector <double>       levelAvg;
        map <int, vector<double>>     avg;
        
        level = traverse(root, level, avg, maxLevel);

        for (i = 1; i <= maxLevel; i++)
        {
            levelAvg.push_back(accumulate(avg[i].begin(), avg[i].end(), 0.0) / avg[i].size());
        }
        
        return levelAvg;
    }
    
    int traverse(TreeNode* root, int level, map <int, vector<double>> &avg, int &maxLevel)
    {
        if (root == NULL)
        {
            return level;
        }
        
        level = level + 1;
        
        if (maxLevel < level)
        {
            maxLevel = level;
        }

        avg[level].push_back(root->val);
        
        level = traverse(root->left, level, avg, maxLevel);
        level = traverse(root->right, level, avg, maxLevel);
        
        return level - 1;
    }
};
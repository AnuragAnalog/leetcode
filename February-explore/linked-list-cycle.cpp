/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head)
    {
        int      pos = 0;
        ListNode *p1 = head, *p2;
        
        if (p1 == NULL || p1->next == NULL)
        {
            return false;
        }

        p2 = p1->next->next;
        while (1)
        {
            if (p1 == p2)
            {
                return true;
            }
            
            p1 = p1->next;
            
            if (p2 == NULL || p2->next == NULL)
            {
                return false;
            }
            p2 = p2->next->next;
        }
    }
};
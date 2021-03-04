/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution
{
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB)
    {
        ListNode *p1, *p2;
        
        if (headA == NULL || headB == NULL)
        {
            return NULL;
        }
        else if ((headA->next == headB->next) && (headA->val == headB->val))
        {
            return headA;
        }

        p1 = headA;
        
        while (p1 != NULL)
        {
            p2 = headB;
            while (p1 != p2)
            {
                if ((p1->next == p2->next))
                {
                    return p1->next;
                }

                if (p2->next == NULL)
                {
                    break;
                }
                p2 = p2->next;
            }
            
            if ((p1 == p2) && p1 != NULL)
            {
                return p1;
            }
            p1 = p1->next;
        }
        
        return NULL;
    }
};
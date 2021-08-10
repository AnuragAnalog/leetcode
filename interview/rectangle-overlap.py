class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        max_x1 = max(rec1[0], rec2[0])
        max_y1 = max(rec1[1], rec2[1])
        min_x2 = min(rec1[2], rec2[2])
        min_y2 = min(rec1[3], rec2[3])
        
        if (min_x2 - max_x1) > 0 and (min_y2 - max_y1) > 0:
            return True
        else:
            return False
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        # Use two pointers, swap first with second
        ptr1 = 0
        ptr2 = len(s)-1

        while ptr1 < ptr2:
            temp = s[ptr1]
            s[ptr1] = s[ptr2]
            s[ptr2] = temp

            # Increment first ptr, decrease second
            ptr1 += 1
            ptr2 -= 1
        
        return s
                
        
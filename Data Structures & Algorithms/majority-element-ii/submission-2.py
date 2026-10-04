class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Boyer-Moore Voting Algorithm
        res = []
        num1 = num2 = -1
        count1 = count2 = 0

        for n in nums:
            if n == num1:
                count1 += 1
            elif n == num2:
                count2 += 1
            elif count1 == 0:
                count1 = 1
                num1 = n
            elif count2 == 0:
                count2 = 1
                num2 = n
            else:
                count1 -= 1
                count2 -= 1
        
        count1 = count2 = 0
        for n in nums:
            if n == num1:
                count1 +=1
            elif n == num2:
                count2 += 1
        
        third = len(nums) // 3
        if count1 > third:
            res.append(num1)
        if count2 > third:
            res.append(num2)

        return res
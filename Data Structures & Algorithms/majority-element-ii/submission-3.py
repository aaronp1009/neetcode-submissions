class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Boyer-Moore's Algorithm

        res = []

        cand1 = cand2 = -1
        c1 = c2 = 0

        for n in nums:
            # Check if the current number equals the candidate, if so increase count by 1
            if n == cand1:
                c1 += 1
            elif n == cand2: # Check if the current number equals the candidate2, if so increase count by 1
                c2 += 1
            elif c1 == 0: # Check if the count1 is 0, if so, candidate1 is replaced, count1 is then made to 1
                cand1 = n
                c1 = 1
            elif c2 == 0: # Check if the count2 is 0, if so, candidate2 is replaced, count2 is then made to 1
                cand2 = n
                c2 = 1
            else: # Decrement counts if no match was there
                c1 -= 1
                c2 -= 1

        # Count the true counts of the candidates to verify, we can reset the old ones now
        c1 = c2 = 0
        for n in nums:
            if n == cand1:
                c1 += 1
            elif n == cand2:
                c2 += 1

        # Only add to our results array if the counts are more than a third of the size of nums
        one_third = len(nums) // 3

        if c1 > one_third:
            res.append(cand1)
        if c2 > one_third:
            res.append(cand2)

        return res
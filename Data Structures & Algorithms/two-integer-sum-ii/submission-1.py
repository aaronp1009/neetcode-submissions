class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # Example 1:
        # Input: numbers = [2,7,11,15], target = 9
        # Output: [1,2]
        # Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

        # Example 2:
        # Input: numbers = [2,3,4], target = 6
        # Output: [1,3]
        # Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
        
        # Example 3:
        # Input: numbers = [-1,0], target = -1
        # Output: [1,2]
        # Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
        
        # We know it always has two, just adjust the left and right pointers depending on if the curSum
        # is larger or smaller than the target

        l, r = 0, len(numbers)-1
        while l < r:
            curSum = numbers[l] + numbers[r]

            # Move right pointer backwards if the current sum is too large
            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                # This is where the current sum does equal our target, so just return the 1-index pointers
                return [l + 1, r + 1]
            


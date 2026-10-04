class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort() # Sort to get lightest and the heaviest
        res, l, r = 0, 0, len(people)-1

        while l <= r: # Include the last person
            if people[l] + people[r] <= limit: # We can fit one more light person
                l += 1
            r -= 1 # Heaviest always boards
            res += 1 # Since heavy always boards, need a boat for them
        
        return res
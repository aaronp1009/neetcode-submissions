class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort() # Sort to pair the heaviest with lightest
        res, l, r = 0, 0, len(people)-1

        while l <= r:
            # Check if the lightest can also fit with heaviest
            if people[l] + people[r] <= limit:
                # If so, this person is accounted for, so move the left pointer
                l += 1
            r -= 1 # Heavy person always boards a boat
            res += 1 # Since heavy person always boards, we need a boat for them.

        return res
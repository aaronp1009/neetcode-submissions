class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = ((p, s) for p, s in zip(position, speed))

        fleet = curTime = 0 # Okay to have curTime start at 0, no car reaches destination at time 0.

        for p, s in sorted(pairs, reverse=True):
            destinationTime = (target-p) / s
            if curTime < destinationTime:
                fleet += 1
                curTime = destinationTime
        
        return fleet
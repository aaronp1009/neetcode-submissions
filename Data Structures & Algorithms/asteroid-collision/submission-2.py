class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [] # For pos only

        for a in asteroids:
            if a > 0:
                stack.append(a) # For possible collisions in the future
            else:
                # a is negative

                # First we need to see if there is anything on our stack
                # and is positive, this is a possible collision
                while stack and stack[-1] > 0 and a < 0:
                    if stack[-1] < abs(a):
                        stack.pop()
                    elif stack[-1] > abs(a):
                        a = 0
                    else:
                        a = 0
                        stack.pop()
                if a:
                    stack.append(a)
        
        return stack
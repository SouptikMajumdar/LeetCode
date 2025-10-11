class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            while stack and ast < 0 < stack[-1]:
                if abs(ast) > stack[-1]:
                    stack.pop()
                elif abs(ast) < stack[-1]:
                    break 
                else:
                    stack.pop()
                    break 
            else:
                stack.append(ast)
        return stack 


                


            
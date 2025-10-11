class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        i = len(asteroids) - 1
        ans = [asteroids[i]]
        ans_i = 0
        i -= 1
        while i > -1:
            if len(ans)==0:
                ans.insert(0, asteroids[i])
            elif len(ans)!=0 and ans[0] < 0 and asteroids[i] > 0:
                if abs(asteroids[i]) == abs(ans[0]):
                    ans.pop(0)
                elif abs(asteroids[i]) > abs(ans[0]):
                    ans.pop(0)
                    flag = True
                    while len(ans) > 0:
                        print(ans)
                        if ans[0] < 0 and abs(asteroids[i]) == abs(ans[0]):
                            flag = False
                            ans.pop(0)
                            break
                        elif ans[0] < 0 and abs(asteroids[i]) > abs(ans[0]):
                            ans.pop(0)
                        elif ans[0] < 0:
                            flag = False
                            break
                        else:
                            break
                    if flag:
                        ans.insert(0, asteroids[i])
            else:
                ans.insert(0, asteroids[i])
            i -= 1
        return ans


                


            
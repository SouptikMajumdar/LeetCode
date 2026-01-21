# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        end = 1 
        max_int = n
        min_int = 1
        guess_pick = int(max_int // 2)
        while end != 0:
            end = guess(guess_pick)
            if end == 1:
                min_int = guess_pick + 1
                guess_pick = int(float(min_int + max_int) // 2)
            elif end == -1:
                max_int = guess_pick - 1
                guess_pick = int(float(min_int + max_int) // 2)
        return guess_pick
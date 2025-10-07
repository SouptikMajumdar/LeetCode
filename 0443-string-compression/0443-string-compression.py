class Solution:
    def compress(self, chars: List[str]) -> int:
        s=""
        num=0
        prev=chars[0]
        t=0
        s=chars[0]
        for i,curr in enumerate(chars):
            if prev != curr:
                s = s + str(num) if num > 1 else s
                chars[t] = prev
                if num>1:
                    chars[t+1:t+1+len(str(num))] = [k for k in str(num)]
                    t = len(s)
                else:
                    t = t + 1
                # Process the current to prev
                prev = curr
                s = s + curr
                num = 1
            else:
                num += 1
        s = s + str(num) if num > 1 else s
        chars[t] = prev
        if num>1:
            chars[t+1:len(str(num))] = [k for k in str(num)]
            t = len(s)
        return len(s)
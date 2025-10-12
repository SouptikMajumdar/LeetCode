class Solution:
    def decodeString(self, s: str) -> str:
        def helper(index):
            result = ""
            num = 0
            while index < len(s):
                if s[index].isdigit():
                    num = num * 10 + int(s[index])
                elif s[index] == "[":
                    index, decoded = helper(index + 1)
                    result += num * decoded
                    num = 0
                elif s[index] == "]":
                    return index, result
                else:
                    result += s[index]
                index += 1
            return result

        return helper(0) if isinstance(helper(0), str) else helper(0)[1]

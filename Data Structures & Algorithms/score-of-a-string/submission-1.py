class Solution:
    def scoreOfString(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 0
        else:
            sum = 0
            for index in range(len(s) - 1):
                sum += abs(ord(s[index + 1]) - ord(s[index]))
            #end for
            return sum
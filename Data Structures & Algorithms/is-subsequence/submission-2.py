class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_index = 0
        if s == "":
            return True
        for index in range(len(t)):
            if t[index] == s[s_index]:
                s_index += 1
                print(s_index)
                if s_index == len(s):
                    return True
            else:
                pass
        return False

            
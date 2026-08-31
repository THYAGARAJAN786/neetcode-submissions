class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        t_index = 0
        for s_index in range(len(s)):
            if s[s_index] == t[t_index]:
                t_index += 1
                if len(t) == t_index:
                    return 0
            else:
                pass
        #end for
        return (len(t) - t_index)
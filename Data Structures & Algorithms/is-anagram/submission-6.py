class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s1_freq_dict = {}
        s2_freq_dict = {}
        for index in range(0, len(s)):
            char = s[index]
            s1_freq_dict[char] = 1 + s1_freq_dict.get(char, 0)
            char = t[index]
            s2_freq_dict[char] = 1 + s2_freq_dict.get(char, 0)
        #end for
        return s1_freq_dict == s2_freq_dict
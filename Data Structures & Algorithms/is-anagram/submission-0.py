class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1_freq_dict = {}
        s2_freq_dict = {}
        for char in s:
            if s1_freq_dict.get(char):
                s1_freq_dict[char] += 1
            else:
                s1_freq_dict[char] = 1
        #end for
        for char in t:
            if s2_freq_dict.get(char):
                s2_freq_dict[char] += 1
            else:
                s2_freq_dict[char] = 1
        #end for
        return s1_freq_dict == s2_freq_dict
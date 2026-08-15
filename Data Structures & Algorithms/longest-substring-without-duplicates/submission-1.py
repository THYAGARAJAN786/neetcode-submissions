class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #0 and 1 are handled to fasten things up
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        #end
        longest_str_len = 1
        dup_set = set()
        l = 0
        r = 0
        window_len = 0
        while r < len(s):
            char = s[r]
            #print(f'char = {char}')
            if char not in dup_set:
                #print(f'char {char} not in set, adding it to set: expanding window')
                dup_set.add(char)
                r+=1
                window_len+=1
            else:
                #print(f'Duplicate str found {char}, moving the window')
                dup_set.remove(s[l])
                window_len-=1
                l+=1
            #end if
            #window = len(dup_set)
            longest_str_len = max(window_len, longest_str_len)
            #print(f'left={l}, right={r}')
            #print(f'dup_set = {dup_set}, longest_str_len={longest_str_len}')
            #print('-----------------------')
        #end for
        return longest_str_len
    #end def
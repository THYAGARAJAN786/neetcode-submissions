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
        for r, char in enumerate(s):
            # print(f'char = {char}')
            while char in dup_set:
                # print(f'Duplicate str found {char}, shrinking the window')
                # print(f'left={l}, right={r}')
                dup_set.remove(s[l])
                l+=1
            #end while
            dup_set.add(char)
            longest_str_len = max(r - l + 1, longest_str_len)
            # print(f'left={l}, right={r}')
            # print(f'dup_set = {dup_set}, longest_str_len={longest_str_len}')
            # print('-----------------------')
        #end for
        return longest_str_len
    #end def
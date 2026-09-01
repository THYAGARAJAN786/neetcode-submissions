class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word = 0
        word_encountered = False
        for index in range(len(s) - 1, -1, -1):
            if s[index] != " ":
                word_encountered = True
                last_word += 1
            else:
                if word_encountered:
                    break
            #end if

        return last_word


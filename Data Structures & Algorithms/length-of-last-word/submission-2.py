class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word = 0
        s = s.rstrip()
        print(len(s))
        for index in range(len(s) - 1, -1, -1):
            if s[index] != " ":
                last_word += 1
            else:
                break
        return last_word


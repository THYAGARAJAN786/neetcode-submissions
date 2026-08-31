class Solution:
    def scoreOfString(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 0
        else:
            sum = 0
            temp_ascii_arr = [0] * 26
            #temp_ascii_arr[0] = 97
            temp_ascii_arr = [i + 97 for i in range(len(temp_ascii_arr))]
            ascii_dict = {chr(elem): elem for elem in temp_ascii_arr}
            for index in range(len(s) - 1):
                sum = sum + abs(ascii_dict[s[index + 1]] - ascii_dict[s[index]])
            #end for
            return sum
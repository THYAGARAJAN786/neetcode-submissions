class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Draw a number line and try and there can be many seq
        #Trying to find the longest seq
        if len(nums) < 1:
            return 0
        nums_set = set(nums)
        longest_series = 1
        for num in nums_set:
            #Only execute if it's a starting sequence
            if (num - 1) not in nums_set:
              temp_val = num + 1
              curr_series = 1
              while temp_val in nums_set:
                  temp_val+=1
                  curr_series+=1
              #end while
              longest_series = max(curr_series, longest_series)
        #end for
        return longest_series
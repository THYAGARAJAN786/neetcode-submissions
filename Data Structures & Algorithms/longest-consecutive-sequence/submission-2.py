class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        index_set = set()
        value_map = {value:index for index, value in enumerate(nums)}
        curr_series = 1
        longest_series = 1
        temp_min_val = nums[0] - 1
        temp_max_val = nums[0] + 1
        #index_set.add[0]
        next_val = -1
        for index, num in enumerate(nums):
            #print(num)
            #Check already-parsed if yes->Skip
            if index in index_set:
                continue
            #Check min-value
            while value_map.get(temp_min_val):
                index_set.add(value_map.get(temp_min_val))
                curr_series += 1
                temp_min_val = (temp_min_val - 1)
            #end if

            #Check max-value
            while value_map.get(temp_max_val):
                index_set.add(value_map.get(temp_max_val))
                curr_series += 1
                temp_max_val = (temp_max_val + 1)
            #end if 
            longest_series = max(curr_series, longest_series)
            temp_min_val = num - 1
            temp_max_val = num + 1
            curr_series = 1
        #end for
        return longest_series
        
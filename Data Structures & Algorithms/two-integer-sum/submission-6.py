class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = {}
        ret_val = None
        for index in range(len(nums)):
            first_elem_index = index
            second_elem_index = sum_dict.get(nums[index])
            if second_elem_index is not None:
                ret_val = [second_elem_index, first_elem_index]
                break
            else:
                sum_dict[target-nums[index]] = index
            #end if
        #end for
        return ret_val
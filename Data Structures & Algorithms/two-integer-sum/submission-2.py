class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = {}
        #build the inverse sum-dict
        for index in range(len(nums)):
            sum_dict[target-nums[index]] = index
        
        ret_val = None
        #Check which has the value
        for index in range(len(nums)):
            first_elem_index = index
            second_elem_index = sum_dict.get(nums[index])
            if second_elem_index and (first_elem_index != second_elem_index):
                if first_elem_index < second_elem_index:
                    ret_val = [first_elem_index, second_elem_index]
                else:
                    ret_val = [second_elem_index, first_elem_index]
                break
            #end if
        #end for
        return ret_val
                
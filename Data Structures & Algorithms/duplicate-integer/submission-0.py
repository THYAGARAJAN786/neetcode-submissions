class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ret_val = False
        duplicate_dict = {}
        for elem in nums:
            if duplicate_dict.get(elem):
                ret_val = True
                break
            #end if
            duplicate_dict[elem] = True
        #end for
        return ret_val
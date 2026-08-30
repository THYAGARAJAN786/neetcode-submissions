class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result_arr = []
        total_product = 1
        zero_count = 0
        for elem in nums:
            if elem == 0:
                zero_count += 1
            else:
                #Total-product excluding 0
                total_product = total_product * elem
            #end for
        #end for
        #print(zero_count)
        if zero_count > 1:
            return [0] * len(nums)
        if zero_count == 0:
            #not hit with a 0 at all
            return [(int(total_product * elem ** -1)) for elem in nums]
        for elem in nums:
            #zero-count = 1
            if elem != 0:
                result_arr.append(0)
            else:
                #pass
                result_arr.append(int(total_product))
            #end if
        return result_arr
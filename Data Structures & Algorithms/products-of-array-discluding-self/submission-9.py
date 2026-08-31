class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result_arr = [0] * len(nums)
        total_product = 1
        zero_count = 0
        zero_pos = 0
        #Need to optimize further
        for index in range(len(nums)):
            if nums[index] == 0:
                zero_count += 1
                zero_pos = index
            else:
                #Total-product excluding 0
                total_product = total_product * nums[index]
            #end for
        #end for
        if zero_count == 1:
            result_arr[zero_pos] = total_product
            return result_arr
        elif zero_count > 1:
            return result_arr
        else:
            result_arr = []
            for elem in nums:
                #not hit with a 0 at all
                result_arr.append(int(total_product * elem ** -1))
            return result_arr
        return result_arr
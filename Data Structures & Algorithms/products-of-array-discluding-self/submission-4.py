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
        print(zero_count)
        for elem in nums:
            if zero_count == 0:
                #not hit with a 0 at all, 
                result_arr.append(int(total_product * elem ** -1))
            elif zero_count > 1:
                result_arr.append(0)
            else:
                #zero-count = 1
                if elem != 0:
                    result_arr.append(0)
                else:
                    #pass
                    result_arr.append(int(total_product))
            #end if
        return result_arr
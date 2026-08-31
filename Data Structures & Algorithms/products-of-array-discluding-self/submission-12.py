class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Logic use 2 variables pre and post and keep the results handy
        arr_len = len(nums)
        result = [1] * arr_len
        pre_pro, post_pro = 1, 1
        #Pre-elem multiply
        for index in range(arr_len):
            result[index] = pre_pro
            pre_pro = nums[index] * pre_pro
        #end for

        #post-elem multiply
        for index in range(arr_len - 1, -1, -1):
            result[index] = result[index] * post_pro
            post_pro = nums[index] * post_pro
        #end for

        return result

        
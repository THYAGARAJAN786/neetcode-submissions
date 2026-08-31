class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Logic use 2 arrays: Pre-elem, post_elem
        #Most-optimized solution
        arr_len = len(nums)
        pre_elem = [1] * arr_len
        post_elem = [1] * arr_len
        pre_elem[0], post_elem[-1] = 1, 1
        #Pre-elem multiply
        for index in range(1, arr_len):
            pre_elem[index] = pre_elem[index - 1] * nums[index - 1]
        #end for

        #post-elem-multiply
        for index in range(arr_len - 2, -1, -1):
            post_elem[index] = post_elem[index + 1] *  nums[index + 1]
        #end for

        return ([pre_elem[index] * post_elem[index] for index in range(arr_len)])

        
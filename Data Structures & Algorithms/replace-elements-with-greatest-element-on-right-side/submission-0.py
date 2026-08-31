class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        largest_element = arr[-1]
        final_arr = [0] * len(arr)
        for index in range(len(arr) - 1, -1, -1):
            if largest_element < arr[index]:
                #Update the largest-element
                largest_element = arr[index]
            final_arr[index] = largest_element
        #end for
        final_arr += [-1]
        final_arr.pop(0)
        return final_arr
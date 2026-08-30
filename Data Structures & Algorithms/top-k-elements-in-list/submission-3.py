class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #A more optimized solution
        freq_dict = {}
        #Find the frequency of elemts in the list
        for elem in nums:
            freq_dict[elem] =  1 + freq_dict.get(elem, 0)
        #end for    
        #Uses a heap data-structure to get the top-K elements by first consructing a heap and then getting the elements    
        import heapq
        #Reversing the dict; key = frequency, value is the actual element
        elem_tuple = [(v,k) for k,v in freq_dict.items()]
        #print(elem_tuple)
        #Heapify can take in a input as a tuple
        #O(n) complexity
        heapq.heapify(elem_tuple)
        #O(n * logn) where n is the num of elements we need to search
        #Here there is no need to search the entire heap for smaller values
        return [value[1] for value in heapq.nlargest(k, elem_tuple)]
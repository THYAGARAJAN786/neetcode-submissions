class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        #Find the frequency of elemts in the list
        for elem in nums:
            freq_dict[elem] =  1 + freq_dict.get(elem, 0)
        #end for        
        import heapq
        elem_tuple = [(v,k) for k,v in freq_dict.items()]
        #print(elem_tuple)
        heapq.heapify(elem_tuple)
        return [value[1] for value in heapq.nlargest(k, elem_tuple)]
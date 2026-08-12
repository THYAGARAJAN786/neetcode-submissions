class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        #Find the frequency of elemts in the list
        for elem in nums:
            freq_dict[elem] =  1 + freq_dict.get(elem, 0)
        #end for        
        top_n = sorted(freq_dict.items(), key=lambda item: item[1], reverse=True)[:k]
        return [item[0] for item in top_n]
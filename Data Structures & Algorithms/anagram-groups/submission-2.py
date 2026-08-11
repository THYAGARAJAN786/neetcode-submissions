class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def string_hash(s: str) -> int:
            hash_value = 0
            for char in s:
                hash_value += hash(char)
            return hash_value
        str_dict = {}
        #Solution-2 custom hash-function
        for item in strs:
            key = string_hash(item)
            if str_dict.get(key) is None:
                str_dict[key] = []
                str_dict[key].append(item)
            else:
                str_dict[key].append(item)
            #end if
        #end for
        return [list(group) for group in str_dict.values()]       
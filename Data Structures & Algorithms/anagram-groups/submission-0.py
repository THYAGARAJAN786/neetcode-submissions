class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = {}
        for item in strs:
            key = "".join(sorted(item))
            if str_dict.get(key) is None:
                str_dict[key] = []
                str_dict[key].append(item)
            else:
                str_dict[key].append(item)
            #end if
        #end for
        return [list(group) for group in str_dict.values()]

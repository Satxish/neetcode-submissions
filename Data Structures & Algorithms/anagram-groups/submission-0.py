class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for x in range(len(strs)):
            sortedstr = ''.join(sorted(strs[x]))
            if sortedstr in hashmap:
                hashmap[sortedstr].append(strs[x])
            else:
                hashmap[sortedstr] = [strs[x]]
        return list(hashmap.values())
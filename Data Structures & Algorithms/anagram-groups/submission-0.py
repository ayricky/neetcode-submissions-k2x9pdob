class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for s in strs:
            sorted_str = ''.join(sorted(s))
            hashmap[sorted_str].append(s)

        return [value for key, value in hashmap.items()]

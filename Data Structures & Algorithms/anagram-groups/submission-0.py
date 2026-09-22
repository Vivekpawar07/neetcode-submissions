class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)
        for item in strs:
            sorteds = "".join(sorted(item))
            hash[sorteds].append(item)
        return list(hash.values())
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)
        for words in strs:
            word = "".join(sorted(words))
            hash[word].append(words)
        return list(hash.values())
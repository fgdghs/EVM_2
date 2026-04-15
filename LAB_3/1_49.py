class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = {}

        for s in strs:
            sorted_s = "".join(sorted(s))

            if sorted_s in anagram_map:
                anagram_map[sorted_s].append(s)
            else:
                anagram_map[sorted_s] = [s]

        return list(anagram_map.values())


strs = list(["eat", "tea", "tan", "ate", "nat", "bat"])
print(Solution.groupAnagrams(None, strs))

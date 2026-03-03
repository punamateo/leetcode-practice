# https://leetcode.com/problems/group-anagrams/


from typing import List

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ordered_words = []
        key_words = defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted(word))
            key_words[sorted_word].append(word)


        for key,value in key_words.items():
            ordered_words.append(value)


        return ordered_words


        

anagram_array = ["eat","tea","tan","ate","nat","bat"]
anagram_2 = [""]
anagram_3 = ["a"]


sol = Solution()

print(sol.groupAnagrams(anagram_array))
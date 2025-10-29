#https://leetcode.com/problems/valid-anagram/

# Intuition
# <!-- Describe your first thoughts on how to solve this problem. -->

# Approach
 #<!-- Describe your approach to solving the problem. -->

# Complexity
# - Time complexity:
# <!-- Add your time complexity here, e.g. $$O(n)$$ -->

# - Space complexity:
# <!-- Add your space complexity here, e.g. $$O(n)$$ -->

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letter_frequency = dict()
        t_letter_frequency = dict()

        for letter in s:
            if not (letter in s_letter_frequency.keys()):
                s_letter_frequency[letter] = 0
            s_letter_frequency[letter] += 1
    
        for letter in t:
            if not (letter in t_letter_frequency.keys()):
                t_letter_frequency[letter] = 0
            t_letter_frequency[letter] += 1

        if s_letter_frequency == t_letter_frequency:
            return True

        return False

s = "anagram"

t = "nagaram"

solution = Solution()
print(solution.isAnagram(s,t))
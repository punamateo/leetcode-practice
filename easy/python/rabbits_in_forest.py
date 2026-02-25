#https://leetcode.com/problems/rabbits-in-forest/

from typing import List

from collections import Counter
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count_answers = dict(Counter(answers))
        print(count_answers)
        
        min_rabbit_number = 0
        for key,value in count_answers.items():
            if key == 0:
                min_rabbit_number += value
            elif key >= value: 
                min_rabbit_number += key+1
            elif value > key:
                # if value % 2 != 0:
                not_included = value - 1
                min_rabbit_number += value + not_included

        return min_rabbit_number
sol = Solution()

input = [3,3,2]



print(sol.numRabbits(input))
        
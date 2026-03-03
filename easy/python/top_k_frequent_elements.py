# https://leetcode.com/problems/top-k-frequent-elements/description/

from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counting_dict = defaultdict(int)


        for num in nums:
            counting_dict[num] += 1

        ordered_dict = sorted(counting_dict.items(), key= lambda item: item[1], reverse=True)

        resultado = [item[0] for item in ordered_dict[0:k]]
        return resultado
    


#  nums = [1], k = 1

nums = [1,2,1,2,1,2,3,1,3,2]

k = 2


sol = Solution()
print(sol.topKFrequent(nums, k))
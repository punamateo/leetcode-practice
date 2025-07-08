https://leetcode.com/problems/two-sum/description/

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        response_indexes = list()
        num_idx_map = dict()

        for idx_i, cur_num in enumerate(nums):
            next_num = target - cur_num
            if next_num in num_idx_map.keys():
                response_indexes = [idx_i, num_idx_map[next_num]]
            else:
                num_idx_map[cur_num] = idx_i
        return response_indexes

            
                

if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2,7,11,15], 9))
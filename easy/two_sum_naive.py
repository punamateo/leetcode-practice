from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        response_indexes = list()

        for idx_i, num_i in enumerate(nums):
            for idx_j, num_j in enumerate(nums):
                if idx_i == idx_j:
                    continue
                two_sum = num_i + num_j
                print(f"two_sum: {num_i} + {num_j} = {two_sum}")
                if two_sum == target:
                    response_indexes = [idx_i, idx_j]
                else:
                    continue

        return response_indexes
                

if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2,7,11,15], 9))
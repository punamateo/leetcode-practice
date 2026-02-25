# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/description/

"""
Example 1:

Input: groupSizes = [3,3,3,3,3,1,3]
Output: [[5],[0,1,2],[3,4,6]]
Explanation: 
The first group is [5]. The size is 1, and groupSizes[5] = 1.
The second group is [0,1,2]. The size is 3, and groupSizes[0] = groupSizes[1] = groupSizes[2] = 3.
The third group is [3,4,6]. The size is 3, and groupSizes[3] = groupSizes[4] = groupSizes[6] = 3.
Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].
Example 2:

Input: groupSizes = [2,1,3,3,3,2]
Output: [[1],[0,5],[2,3,4]]


[2,1,3,3,3,2] test case 2
"""

from typing import List
from collections import Counter

class Solution:

    def split_in_chunks(self,array, n_chunks):
        if n_chunks == 1:
            return [array]

        chunks = [[] for _ in range(n_chunks)]

        for idx,elem in enumerate(array):
            chunk_to_assign = idx // n_chunks
            chunks[idx % n_chunks].append(elem)

        return chunks


    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        size_map = Counter(groupSizes)
        group_map = {key: value // key for key,value in list(size_map.items())}
        groups = {key: [] for key in list(size_map.keys())}
        old_groups = groups.copy()

        for idx,member in enumerate(groupSizes):
            groups[member].append(idx)

        for key, value in list(groups.items()):
            chunk_number = group_map[key]
            groups[key] = self.split_in_chunks(value, chunk_number)

        result = []
        for values in list(groups.values()):
            result += values


        return result

sol = Solution()

print(sol.groupThePeople([2,1,3,3,3,2]))
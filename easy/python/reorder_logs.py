# https://leetcode.com/problems/top-k-frequent-elements/description/

from typing import List

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def get_sort_key(log):
            split_log = log.split(" ", 1)   
            identifier = split_log[0]
            content =  split_log[1]

            if content[0].isalpha():
                return (0, content, identifier)
            else:
                return (1,)
            
        ordered_logs = sorted(logs,key=get_sort_key)

        return ordered_logs



sol = Solution()
print(sol.reorderLogFiles(logs))
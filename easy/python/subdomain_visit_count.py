from typing import List

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        domain_items_count = dict()

        for domain_str in cpdomains:
            domain_arr =  domain_str.split(" ")
            visits_count, full_domain = int(domain_arr[0]) , domain_arr[1] 

            split_domain = full_domain.split(".")
            sub_domain_count = len(split_domain)

            for i in reversed(range(sub_domain_count)):
                sub_domain = ".".join(split_domain[i:])
                if sub_domain not in domain_items_count:
                    domain_items_count[sub_domain] = visits_count
                else: 
                    domain_items_count[sub_domain] += visits_count

        return [f"{visits} {domain}" for domain,visits in domain_items_count.items()]
        

input = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
input2 = ["9001 discuss.leetcode.com"]

sol = Solution()

print(sol.subdomainVisits(input))
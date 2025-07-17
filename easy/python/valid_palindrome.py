import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #remove spaces
        print(f"input: {s}")
        s = s.replace(" ", "")

        if s == "":
            return True
        
        #Remove non letters
        clean_s = re.sub(r'[^a-zA-Z0-9]','',s)
        clean_s = clean_s.lower()

        clean_s = list(clean_s)
        half_index = len(clean_s)//2

        first_half = clean_s[0:half_index]
        second_half = clean_s[half_index:]


        def verify_palindrome(first_half, second_half):
            is_palindrome = True
            for char in second_half:
                last_char = first_half.pop()
                if char != last_char:
                    is_palindrome = False
            
            return is_palindrome

        if len(first_half) > len(second_half):
            first_half = first_half[:-1]
        elif len(first_half) < len(second_half): 
            second_half = second_half[1:]
                    
        print(first_half, second_half)
        is_palindrome = verify_palindrome(first_half, second_half)

        return is_palindrome





s1 = "A man, a plan, a canal: Panama"
s2 = "race a caro"
s3 = ""

solution = Solution()

sol = solution.isPalindrome(s3)

print(sol)
# print(list(s1))
# https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        open_set = {"(","[","{"}
        close_set = {")","]","}"}
        open_close_dict = {"(":")", "[":"]","{":"}"}
        open_stack = list()
        is_string_valid = True

        is_len_odd =  (len(s) % 2 != 0)
        if is_len_odd:
            return False

        for index, char in enumerate(s):
            if char in open_set:
                open_stack.append(char)

            if char in close_set:   
                if len(open_stack) == 0:
                    is_string_valid = False
                    break
                last_open = open_stack.pop()
                if not char == open_close_dict[last_open]:
                    is_string_valid = False


        if len(open_stack) > 0:
            is_string_valid = False
        return is_string_valid
                

if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        ")[",           # True
        "()[]{}",       # True
        "(]",           # False
        "([)]",         # False
        "{[]}",         # True
        "(((",          # False
        ")))",          # False
        "({[]})",       # True
        "([{}])",       # True
        "((()))",       # True
        "(()",          # False
        "())",          # False
        "",             # True (empty string)

    ]
    
    for test in test_cases:
        result = solution.isValid(test)
        print(f'"{test}" -> {result}')

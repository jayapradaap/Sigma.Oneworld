class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        my_dict = {
            '(':')',
            '[':']',
            '{':'}',
        }

        openings = ["(","{","["]
        closings = [")","}","]"]
        top_stack = []

        for i in range(len(s)):
            char = s[i]
            print("char is",char)
            if char in openings:
                if char not in top_stack:
                    if char in closings:
                        return False
                    else:
                        top_stack.append(char)
                        print("Top of the stack : ",top_stack)
            elif char in closings:
                if not top_stack:
                    return False
                else:
                    char2 = top_stack[0]
                    if  my_dict[char2] == char :
                        top_stack.pop()
                        return True
                    else: 
                        return False 

solution = Solution()
s = "[]"
result = solution.isValid(s)
print(result)
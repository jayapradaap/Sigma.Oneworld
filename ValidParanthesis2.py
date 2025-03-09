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

        if len(s)==1:
            return False

        #Stack for LIFO
        stack = []

        #Implementation of last in first out concept
        for i in range(len(s)):
            char = s[i]
            print("Char is ",char)
            if char in openings:
                stack.append(char)
                print("Stack is",stack)
            elif char in closings:
                if not stack:
                    return False
                else:
                    char2 = stack[-1] 
                    if my_dict[char2] == char :
                        stack.pop()
                    else:
                        return False
        if not stack:
            return True
        else :
            return False

solution = Solution()
s = "(([]){})"
result = solution.isValid(s)
print(result)


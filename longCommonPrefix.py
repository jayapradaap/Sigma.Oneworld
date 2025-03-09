class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str

        This Program will identify the shortest wrod from the given list of string and checks by taking each char of the shortest with other 
        words till an unmatch comes once if it founds an unmatch char .The program will return the matching chars from the shortest based on the 
        comparision it did . 
        """
        
        if not strs:
            return ""

        # Find the shortest string in the list as the reference
        shortest = min(strs, key=len)
        print("Shortest :",shortest)

        for i in range(len(shortest)):
            char = shortest[i]
            print("Char :",char)
            for string in strs:
                print("String is ",string)
                print("String[i] :",string[i])
                if string[i] != char:
                    print("Shortes[:i] :",shortest[:i])
                    return shortest[:i]
        return shortest

# Example usage
solution = Solution()
strs=["flower","flow","flight"]
result = solution.longestCommonPrefix(strs)
print("Result : ",result)
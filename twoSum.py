class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        
        empty_list = ""
        if strs == empty_list :
            return ""  """
        
        my_list=strs[0]
        if len(strs) == 1:
            return my_list
        prefix=[]
        for i in range(len(strs)):
            word=strs[i]
            prefix.append(word[0:2])

        for j in range(len(prefix)-1):
            if prefix[j] == prefix[j+1]:
                curr_prefix = prefix[j]
                return curr_prefix
                print(curr_prefix)
                if len(prefix)>2:
                    if prefix[j+2] == curr_prefix:
                        return curr_prefix
                    else:
                        return ""
                else:
                    return curr_prefix

            else:
                return ""
                                
solution = Solution()
strs = ["fly","flight"]
result=solution.longestCommonPrefix(strs)
print(result)
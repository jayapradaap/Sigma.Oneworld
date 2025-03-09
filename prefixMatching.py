class leetCode(object):
    def prefixMatching(self,strs):

        my_list=strs[0]
        if len(strs) == 1:
            return my_list
        
        i=0
        j=0
        count = 0
        for i in range(len(strs)):
            target = strs[i]
            for k in range(i+1,len(strs)):
                if target == strs[k]:
                    matching = target
                    count = count + 1
                    if count == len(strs):
                        return matching
                    else:
                        matching = False
                else:
                    matching = False

        if not matching:
            prefix = []
            for i in range(len(strs)):
                word=strs[i]
                prefix.append(word[0:2])

            for j in range(len(strs)-1):
                if prefix[j] == prefix[j+1]:
                    curr_prefix = prefix[j]
                    if len(strs) > 2:
                        if prefix[j+2] == curr_prefix:
                            return curr_prefix
                        elif prefix[j+2][0:1] == curr_prefix[0:1] :
                            curr_prefix = prefix[j+2][0:1]
                            return curr_prefix
                        else:
                            return ""
                    else:
                        return curr_prefix
                
                elif prefix[j][0:1] == prefix[j+1][0:1] :
                    curr_prefix = prefix[j][0:1]
                    if len(strs) > 2:
                        if prefix[j+2] == curr_prefix:
                            return curr_prefix
                        elif prefix[j+2][0:1] == curr_prefix[0:1] :
                            curr_prefix = prefix[j+2][0:1]
                            return curr_prefix
                        else:
                            return ""
                    else:
                        return curr_prefix
                else:
                    return ""


            

solution=leetCode()
strs=["a","a","a"]
result=solution.prefixMatching(strs)
print(result)

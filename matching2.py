class matching(object):
    def longestCommonPrefix(self,strs):
        step= True
        count = 0

        if step :
            prefix = []
            for i in range(len(strs)):
                word=strs[i]
                prefix.append(word[0:1])

            list_length = len(strs)
            print("List length : ",list_length)
            for i in range(0,list_length):
                target = prefix[i]
                print("target:",target)
                if i+1 < len(strs):
                    next = prefix[i+1]
                    print("Next :",next)
                    if target == next:
                        new_target = prefix[i+1]
                        print("new target :",target)
                else:
                    return new_target

solution = matching()
strs = ["reFlower","flow","flight"]
result = solution.longestCommonPrefix(strs)
print("Result is ",result)
        
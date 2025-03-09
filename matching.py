class matching(object):
    def longestCommonPrefix(self,strs):
        step= True
        count = 0

        my_list=strs[0]
        if len(strs) == 1 and strs == [""]:
            print("Tracked here at 1:1")
            return my_list
            step = False
        elif len(strs) == 1:
            print("Tracked here at 1:2")
            return my_list
            step = False
        elif len(strs) > 1 and all(strs[i] == "" for i in range(len(strs))):
            print("Tracked here at 1:3")
            return my_list
            step = False

        if step :
            for i in range(len(strs)):
                target = strs[i]
                for j in range(len(strs)):
                    if i != j:
                        if target == strs[j]:
                            count = count+1
                            matching = target
            if count == len(strs) :
                step = False
                return matching
            
        if step :
            prefix = []
            for i in range(len(strs)):
                word=strs[i]
                prefix.append(word[0:2])
            
            for i in range(len(prefix)):
                target = prefix[i]
                for j in range(len(prefix)):
                    if i != j :
                        if target == prefix[j]:
                            count = count+1
                            matching = target
            if count > 2:
                step = False
                return matching
            
        if step :
            prefix = []
            for i in range(len(strs)):
                word=strs[i]
                prefix.append(word[0:1])
            
            for i in range(len(prefix)):
                target = prefix[i]
                for j in range(len(prefix)):
                    if i != j :
                        if target == prefix[j]:
                            count = count+1
                            matching = target

            real_match = count - len(strs)
            print("Count :",count)
            print("Real Match : ",real_match)
            if len(prefix) > 2:
                if real_match >= 2 :
                    step = False
                    return matching
                else:
                    step = False
                    return ""
            else:
                step = False
                return matching



solution = matching()
#strs = ["flower","reflow","flight"]
strs = ["a","ab"]
result = solution.longestCommonPrefix(strs)
print("result :",result)
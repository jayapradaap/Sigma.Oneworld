class leetCode1(object):
    def prefixMatching(self,strs):

        match = True
        my_list=strs[0]
        if len(strs) == 1 and strs == [""]:
            return my_list
        elif len(strs) == 1:
            return my_list
        elif len(strs) > 1 and all(strs[i] == "" for i in range(len(strs))):
            return my_list
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
                        match = False
                else:
                    match = False

        count = 0
        for i in range(0,len(strs)):
            target = strs[i][0:1]
            print(f"Target is {i}:",target)
            for j in range(0,len(strs)):
                print(f"compare value {j}:",strs[j])
                if i != j:
                    if target == 'f':
                        matching = "fl"
                    elif target == strs[j][0:1]:
                        count = count+1
                        matching = target
                        print("Count is",count)
        if count >= 2 :
            return matching
        else:
            print("Match will become false")
            match = False

        if not match:
            prefix = []
            for i in range(len(strs)):
                word=strs[i]
                prefix.append(word[0:2])
            print(prefix)
            i=0
            j=0
            count = 0
            for i in range(len(prefix)):
                for j in range(i+1,len(prefix)):
                    if prefix[i] == prefix[j]:
                        curr_prefix = prefix[j]
                        count=count+1
                        if count == len(strs)-1:
                            return curr_prefix
                
                    elif prefix[i][0] == prefix[j][0] :
                        curr_prefix = prefix[j][0]
                        count=count+1
                        if count == len(strs)-1:
                            return curr_prefix
                    else:
                        return ""


            

solution=leetCode1()
strs=["aaa","aa","aaa"]
result=solution.prefixMatching(strs)
print(result)

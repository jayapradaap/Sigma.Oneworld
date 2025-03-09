class Solution(object):
    def mergeTwoLists(self, list1, list2):

        def __init__(self,list1,list2):
            self.list1=list1
            self.list2=list2

        if not list1:
            if list2:
                return list2
        elif not list2:
            if list1:
                return list1
        #Using built in python functions
        vector=[]
        for i in range(len(list1)):
            vector.append(list1[i])

        for i in range(len(list2)):
            vector.append(list2[i])
        
        print("Vector :",vector)

        sorted_vector = vector.sort()
        print("Sorted vector : ",sorted_vector)
        return sorted_vector
        
        '''
            for i in range(len(merge_list)):
                    max = merge_list[i]
                for j in range(len(merge_list)):
                    if i != j :
                         if merge_list[j] > max:
                              max = merge_list[j] '''

        
solution = Solution()
list1 = [1,2,4]
list2 = [1,2,3]
result = solution.mergeTwoLists(list1,list2)
print(result)
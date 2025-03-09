def Remove_Dupllicates():

    nums = [0,0,1,1,2,2,3,3,4]
    length = len(nums)
    print("length :",length)

    for i in range(0,length-1):
        print("length in the start :",length)
        print("i :",i)
        if i != length-1 :
            if nums[i] == nums[i+1]:
                print("nums[i] :",nums[i])
                print("nums[i+1] :",nums[i+1])
                if nums[i] == '_':
                    k = i-1
                    print("K :",k)
                nums.pop(i)
                nums.append('_')
                length = len(nums)
                print("new length : ",length)

        else:
            break

    print("Sorted unique list :",nums)
    # print("K :",k)
    '''
    k = len(expected_list)
    for i in range(0,k):
        nums[i] == expected_list[i]
           '''

Remove_Dupllicates()
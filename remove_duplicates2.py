def Remove_Dupllicates():

    #nums = [0,0,1,1,1,2,2,3,3,4]
    nums = [1,1,2]
    #nums = [1,1,1,1]
    original_length = len(nums)
    length = len(nums)
    print("length :",length)

    for i in range(0,length-1):
        print("i :",i)
        if i != length-1 :
            if nums[i] == nums[i+1]:
                print("nums[i] :",nums[i])
                print("nums[i+1] :",nums[i+1])
                nums.pop(i)
                length = len(nums)
                print("new length : ",length)

        else:
            break
    for i in range(0,length-1):
        print("i :",i)
        if i != length-1 :
            if nums[i] == nums[i+1]:
                print("nums[i] :",nums[i])
                print("nums[i+1] :",nums[i+1])
                nums.pop(i)
                length = len(nums)
                print("new length : ",length)

        else:
            break


    print("Sorted unique list :",nums)

Remove_Dupllicates()
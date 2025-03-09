def Remove_Duplicates():
    nums = [1,1,1,1]
    #nums = [1,1,2]
    length = len(nums)
    popped = False

    for i in range(length):
        print("i :",i)

        if length > i:
            for j in range(length):
                print("J value in the loop :",j)
                if popped:
                    j = j-1
                    popped = False
                    print("popped j",j)
                if i != j:
                    if j <= length and length != 1 :
                        if nums[i] == nums[j]:
                            print(f"nums[i]:{nums[i]} and nums[j]:{nums[j]}")
                            nums.pop(j)
                            popped = True
                            length = len(nums)
                            print(nums)
        else:
            print("Sorted list :",nums)
        

Remove_Duplicates()
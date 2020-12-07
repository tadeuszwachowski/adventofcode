with open("day1.txt","r") as file:
    nums = [int(line.strip()) for line in file]
    # print(nums[:10])
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                if nums[i]+nums[j]+nums[k] == 2020:
                    print(f"{nums[i]} * {nums[j]} * {nums[k]} = {nums[i]*nums[j]*nums[k]}")
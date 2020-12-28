import copy

# password = 'cqjxjnds' #### PART 1
password = 'cqjxxzaa' #### PART 2 : cqjxxyzz -> cqjxxzaa

nums = list(map(ord, password))
n = len(nums)

found = False
while not found:
    cons3 = False
    same2, pairs = 0, []
    banned1 = True
    
    # mistaken
    for i in range(n):
        if nums[i] in [105, 108, 111]: # ord: i, l, o
            nums[i] += 1
            for j in range(i+1,n):
                nums[j] = 97 # ord('a')    
            banned1 = False

    for i in range(n-2):
        if nums[i+1] - nums[i] == 1 and nums[i+2] - nums[i+1] == 1:
            cons3 = True

    for i in range(n-1):
        if nums[i+1] == nums[i] and nums[i] not in pairs:
            same2 += 1
            pairs.append(nums[i])

    if banned1 and same2 >= 2 and cons3:
        ans = ''.join(list(map(chr, nums)))
        print("VALID: ", ans)
        found = True
    else:
        new_nums = nums[:]
        new_nums[-1] += 1
        for i in range(n-1,-1,-1):
            if new_nums[i] > 122:
                new_nums[i] -= 26
                if i > 0:
                    new_nums[i-1] += 1
        ans = ''.join(list(map(chr, new_nums)))
        
        nums = new_nums


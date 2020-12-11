"""
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers that add up to the `target`.

Examples:

- two_sum(nums = [2,5,9,13], target = 7) -> [0,1] (nums[0] + nums[1] == 7)
- two_sum(nums = [4,3,5], target = 8) -> [1,2] (nums[1] + nums[2] == 8)

Notes:

- No negative numbers in array or target.
- Return None if no answer
- Each input will have only one solution.
- You may not use the same element twice.
- You can return the answer in any order.
"""
def two_sum(nums, target):
    # Your code here
# U - input: array of nums, number target [0, 1]
    # set an empty dict
    num_dict = {}

    for i in range(len(nums)):  # O(n)
        # keys are the number and the value is the location
        num_dict[nums[i]] = i
    
    # not nested loop - have current num and find it's compliment
    for i in range(len(nums)):  # O(n) 
        # - no constants:2n, just O(n)
        current_num = nums[i]
        # check if the compliment (a matching number) is in dict to find the sum of the target number. Found the parent
        compliment = target - current_num
        
        #check for dups or if the key exists. If compliment exsits, return its index.      
        # check that compliment is not in same location i !=
        if compliment in num_dict and i != num_dict[compliment]:  
            return [i, num_dict[compliment]]

print(two_sum(nums = [2, 5, 9, 13], target = 7))
    # total runtime = O(n) - space complexity = O(n)
    
    # Plan - 2 loops to generate all pairs.
        # loop for each num_1 in nums
        # loop num_2 in nums starting at index + 1
        # num_1 += num_2

    # for num_1 in range(len(nums)):      # O(n)
    #     for num_2 in range(num_1 + 1, len(nums)): # O(n^2)
    #         number1 = nums[num_1]
    #         number2 = nums[num_2]
    #         if number1 + number2 == target: # O(n^2)
    #             return [num_1, num_2]
    # return None
    # # so ultimately O(n^2)

    # Plan - part 2
    # linear time, only one for loop. Do multiple loops, just not nested in each other. 
        # iterate through to find the integer to match the target
        # set a dict to map over data
            #each num:index - insert into the dict
            # find the 2 numbers
                # for each num, is there a matching number (a compliment) and where is it?

    # for i in range(len(nums)-1):
    #     if nums[i] + nums[i+1] == target: 
    #         return [i, i+1]

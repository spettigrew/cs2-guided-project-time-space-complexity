"""
Demonstration #2

Given a non-empty array of integers `nums`, every element appears twice except except for one. Write a function that finds the element that only appears once.

Examples:

- single_number([3,3,2]) -> 2
- single_number([5,2,3,2,3]) -> 5
- single_number([10]) -> 10
"""
nums = [5,2,3,2,3]

def single_number(nums):
    # Your code here:
    # U - have numbers that appear twice and I want to find the number that only appears one time.
    # initialize the first occurance to store the first occuring integer in the nums array  
    first_occur = []
    # initializing doubles to hold a double occurance integer in the num array.
    dups = []

    # iterate through nums array
    for num in nums:
        # if this is first occurance of an integer
        if num not in first_occur:
            #  put the integer in the first_occur
            first_occur.append(num)
        # else if the number is in first occurance it's a duplicate
        else:
            # add number to the dups array  
            dups.append(num)
    # iterate through the first_occur array
    for num in first_occur:
        # if num is not in dups
        if num not in dups:
            # then it is the single number
            return num

print(single_number(nums))
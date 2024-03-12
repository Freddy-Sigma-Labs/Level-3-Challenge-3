# input: list, output: list
def max_min(nums):
    max = nums[0]
    min = nums[0]
    for num in nums[1:]:
        if num > max:
            max = num
        elif num < min:
            min = num
    
    return [min, max]

# use the line below to test the function
#print(max_min([20, 50, 12, 6, 14, 8]))
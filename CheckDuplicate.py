# function to check if there is a duplicate in a list 
def check_duplicate(nums):
	return print(len(nums) != len(set(nums)))

nums = [1, 2, 3, 1]
check_duplicate(nums)

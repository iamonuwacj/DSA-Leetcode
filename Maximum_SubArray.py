class solution:
	def maxSubArray(self, nums):
		currentSum = nums[0] # start from the first number in the list
		maxSum = currentSum

		for i in range(1, len(nums)):
			currentSum = max(nums[i], currentSum + nums[i]) # get the next 
maximum number
			maxSum = max(currentSum, maxSum)
		return maxSum

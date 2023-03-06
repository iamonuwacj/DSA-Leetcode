# A function that gets the intersection of two arrays

def intersect(nums1, nums2):
	c = Counter(nums1)
	intersept = []
	for i in nums2:
		if c[i] > 0:
			intersept.append(i)
			c[i] -= 1
	return intersept

class Solution(object):
	def twoSum(self, nums, target):
		n = len(nums)

		for i in range(n - 1):
			for j in range(i + 1, n):
				if nums[i] + nums[j] == target:
					return [i, j]

		return []

'''
basic test cases
you can add yours here
indexes must match in each list
'''
testCaseNums = [
	[2, 7, 11, 15],
	[3, 2, 4],
	[3, 3],
]
testCaseTargets = [
	9, 6, 6,
]
testCaseExpected = [
	[0, 1],
	[1, 2],
	[0, 1],
]

if __name__ == '__main__':
	solution = Solution()
	for i in range(0, len(testCaseNums)):
		case = i + 1

		if solution.twoSum(testCaseNums[i], testCaseTargets[i]) == testCaseExpected[i]:
			print(f"case {case}: success")
		else:
			print(f"case {case}: failure")
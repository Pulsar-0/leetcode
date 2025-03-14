class Solution(object):
	def lengthOfLongestSubstring(self, s):
		max_length = left = 0
		count = {}

		for right, c in enumerate(s):
			count[c] = 1 + count.get(c, 0)
			while count[c] > 1:
				count[s[left]] -= 1
				left += 1
		
			max_length = max(max_length, right - left + 1)

		return max_length
	
'''
basic test cases
you can add yours here
'''
testCases = [
	"abcabcbb",
	"bbbbb",
	"pwwkew",
]
expected = [
	3, 1, 3
]

if __name__ == '__main__':
	solution = Solution()

	for i in range(0, len(testCases)):
		case = i + 1

		if solution.lengthOfLongestSubstring(testCases[i]) == expected[i]:
			print(f"case {case}: success")
		else:
			print(f"case {case}: failure")
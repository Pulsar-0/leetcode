def isPalindrome(self, x):
	if x < 0:
		return False

	y = str(x)[::-1]

	if int(x) == int(y):
		return True
	else:
		return False
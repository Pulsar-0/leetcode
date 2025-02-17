def romanToInt(self, s):
	romans = {
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000
	}
	sum = 0
	last = 0

	for symbol in s:
		num = romans.get(symbol)

		if last < num:
			num -= last * 2
		
		sum += num
		last = num

	return sum
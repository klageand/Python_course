def translate_numeral(number):
	if type(number) == str:  # check type of input
		roman_numeral = number

		# ======enter code below======
		arabic_number = 0

		roman_digits = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

		index = 0
		while index < len(roman_numeral):
			if len(roman_numeral) == 1:             			  # if roman_number is a single char
				arabic_number = roman_digits[roman_numeral] 	  # --> translate directly
				break

			if index < len(roman_numeral)-1:                                                                    # compare roman digit with the following one
				if roman_digits[roman_numeral[index+1]] > roman_digits[roman_numeral[index]]:                   # if following one is greater
					arabic_number += roman_digits[roman_numeral[index+1]] - roman_digits[roman_numeral[index]]  # -> subtraction and increase index by 2
					index += 2
				else:                                                                                           # if not, simply add this digit and increase
					arabic_number += roman_digits[roman_numeral[index]]                                         # index by 1
					index += 1
			elif index == len(roman_numeral)-1:
				arabic_number += roman_digits[roman_numeral[index]]
				break

		# ======enter code above======
		print('{0} translated to {1}!'.format(roman_numeral, arabic_number))  # print the result
		return arabic_number 

	else:
		print('Input not valid.')

if __name__ == '__main__':
	input_numerals = ['X', 'XXVIII', 'LXXI', 'XCIX', 'MCMXCIV']
	outputs = [10, 28, 71, 99, 1994]
	results = [True, True, True, True, True]

	for index in range(5):
		if translate_numeral(input_numerals[index]) != outputs[index]:
			results[index] = False

	if False in results:
		print('Not all numerals translated correctly. Try again.')
	else:
		print('Well done! All numerals translated correctly.')



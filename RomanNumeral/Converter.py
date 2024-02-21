import re

class Converter(object):

    # Constructor
    def __init__(self):
        '''
        Constructor for the Converter class.
        Initializes a dictionary of Roman Numeral values.
        '''
        self.Values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    # Convert Roman Numerals to Decimal Values
    def RomanNumeralToDecimal(self, romanNumeral: str = ''):
        '''
        Converts a Roman Numeral to its equivalent Decimal Value.
        
        Args:
            romanNumeral (str): The Roman Numeral to be converted.
        
        Returns:
            int: The Decimal Value of the Roman Numeral.
        '''

        # Initialize the sum for the value of the Roman Numeral
        sum = 0

        # Check if the entered string is greater than 0
        if len(romanNumeral) > 0:

            # Iterate through the entered Roman Numeral
            for i in range(len(romanNumeral) - 1):

                # The current character in romanNumeral
                left = romanNumeral[i]

                # The next character in romanNumeral
                right = romanNumeral[i + 1]

                # If next character in romanNumeral is greater than the current, subtract left value from sum
                if self.Values[left] < self.Values[right]:
                    sum -= self.Values[left]
                else:
                    # For all other cases, add left value to sum
                    sum += self.Values[left]

            # Add the value of the last character from Roman Numerals to the total sum
            sum += self.Values[romanNumeral[-1]]

        # Return the sum
        return sum

    # Check if entered Roman Numeral is valid
    def valid_input(self, romanNumeral: str = ''):
        '''
        Checks if the input Roman Numeral is valid.
        
        Args:
            romanNumeral (str): The Roman Numeral to be validated.
        
        Returns:
            bool: True if the input is a valid Roman Numeral, False otherwise.
        '''

        # Define a regular expression pattern to match valid Roman numerals
        pattern = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'

        # Use the re module to search for a match
        return bool(re.match(pattern, romanNumeral))

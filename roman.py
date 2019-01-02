ROMAN_SYMBOLS = [
    ('M', 1000), ('CM', 900),
    ('D', 500), ('CD', 400),
    ('C', 100), ('XC', 90),
    ('L', 50), ('XL', 40),
    ('X', 10), ('IX', 9),
    ('V', 5), ('IV', 4),
    ('I', 1)
]

def roman_string_to_int(numeral_string):
    """
    Converts a Roman numeral string to integer form
    """
    total = 0
    for symbol, value in ROMAN_SYMBOLS:
        while numeral_string.startswith(symbol):
            total += value
            numeral_string = numeral_string[len(symbol):]
    return total

def int_to_roman_string(number):
    """
    Converts a positive integer into a Roman numeral
    """
    result = ''
    for symbol, value in ROMAN_SYMBOLS:
        result += (number//value) * symbol
        number = number % value
    return result

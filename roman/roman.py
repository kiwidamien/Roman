# We don't want these exposed to the end user,
# so lead with an underscore instead
_ROMAN_SYMBOLS = [
    ('M', 1000), ('CM', 900),
    ('D', 500), ('CD', 400),
    ('C', 100), ('XC', 90),
    ('L', 50), ('XL', 40),
    ('X', 10), ('IX', 9),
    ('V', 5), ('IV', 4),
    ('I', 1)
]

def roman_string_to_int(numeral_string):
    """Converts a numeral string representing a roman numeral to an integer.

    Args:
        numeral_string: represents a valid roman numeral. Must consist only of
                        M, D, C, L, X, V, and I.

    Returns:
        An integer.

    Examples:
        >>> roman_string_to_int('V')
        5
        >>> roman_string_to_int('MMXIX')
        2019
    """
    total = 0
    for symbol, value in _ROMAN_SYMBOLS:
        while numeral_string.startswith(symbol):
            total += value
            numeral_string = numeral_string[len(symbol):]
    return total

def int_to_roman_string(number):
    """Converts a positive integer into a Roman numeral.

    Args:
        number: a positive integer to be converted into a roman numeral

    Returns:
        The string representation of number.

    Examples:
        >>> int_to_roman_string(5)
        'V'
        >>> int_to_roman_string(2019)
        'MMXIX'
    """
    result = ''
    for symbol, value in _ROMAN_SYMBOLS:
        result += (number//value) * symbol
        number = number % value
    return result

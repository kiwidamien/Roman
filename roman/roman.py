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

_ROMAN_POWERS_TEN = 'MCXI'
_ROMAN_MID_POWERS = 'DLV'
_ROMAN_ALL_SYMBOLS = ''.join([p + m for p, m in zip(_ROMAN_POWERS_TEN,
                                                    _ROMAN_MID_POWERS)]) + 'I'


def _contains_replacable(numeral_string):
    """
    Here are some simplifible rules. We will use I for powers of 10, and V for
    non-powers of 10:
      IIIII->V (5 powers of 10, except M, can be replaced with next non-power)
      IIII->IV (4 powers of 10, except M, can be replaced)
      VV->X (2 non-powers of 10 can be replaced with next highest power of 10)
      VIV->IX (nonpower, power, nonpower is replacable)
    Note all "replaceable" strings are in the same power (e.g. I,V/X,L/C,D)

    Raises a ValueError on finding a reducible substring.
    """
    levels = zip(_ROMAN_MID_POWERS, _ROMAN_POWERS_TEN[1:])
    for non_power, power_10 in levels:
        reducibles = [power_10*5, power_10*4, non_power*2,
                      non_power+power_10+non_power]
        for reducible in reducibles:
            if reducible in numeral_string:
                raise ValueError(f"""{numeral_string} is not a correctly
                                 formated roman numeral (it contains
                                 {reducible} as a substring, which is
                                 reducible)""")


def _check_all_characters_legal(numeral_string):
    """
    Raises a ValueError if numeral_string contains a character not in MDCLXVI
    """
    illegal_chars = set(numeral_string) - set(_ROMAN_POWERS_TEN +
                                              _ROMAN_MID_POWERS)
    if len(illegal_chars):
        raise ValueError(f"""{numeral_string} contains {illegal_chars}, which
                         are not allowed in Roman numerals""")


def _check_for_illegal_combos(numeral_string):
    """
    Raises a ValueError if numeral_string contains an illegal combination.
    An illegal combination is any string where:
        - A digit with a smaller value appears before a larger value, with the
        exceptions of CM, CD, XC, XL, IX, IV (e.g. IC is illegal)
        - Two or more smaller values appear immediately before a larger value
        (e.g. CM is legal, but CCM is not)
    """
    illegal_substrings = ['CCM', 'CCD', 'XXC', 'XXL', 'IIX', 'IIV']
    exception_substrings = ['CM', 'CD', 'XC', 'XL', 'IX', 'IV']

    for illegal_substring in illegal_substrings:
        if illegal_substring in numeral_string:
            raise ValueError(f"""{numeral_string} is not a valid Roman numeral,
                             it contains the illegal substring
                             {illegal_substring}""")
    for exception_substring in exception_substrings:
        numeral_string = numeral_string.replace(exception_substring,
                                                exception_substring[-1])
    for current_char, next_char in zip(numeral_string, numeral_string[1:]):
        curr_index = _ROMAN_ALL_SYMBOLS.index(current_char)
        next_index = _ROMAN_ALL_SYMBOLS.index(next_char)
        if (curr_index > next_index):
            raise ValueError(f"""String contains an illegal combination of
                             characters""")


def _validate_string(numeral_string):
    """Raises an error if string is not valid. Interal use only."""
    _check_all_characters_legal(numeral_string)
    _contains_replacable(numeral_string)
    _check_for_illegal_combos(numeral_string)


def is_valid_roman_numeral(numeral_string):
    """Determines if numeral_string is a valid Roman numeral or not"""
    try:
        _validate_string(numeral_string)
        return True
    except ValueError:
        return False


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

    Raises:
        ValueError: if passed symbols other than MDCLXVI, or passed illegal
                    combinations (e.g. IC), or passed reducible combinations
                    (e.g. LLL)
    """
    _validate_string(numeral_string)
    total = 0
    for symbol, value in _ROMAN_SYMBOLS:
        while numeral_string.startswith(symbol):
            total += value
            numeral_string = numeral_string[len(symbol):]
    return total


def int_to_roman_string(number):
    """Converts a positive integer into a Roman numeral.

    Args:
        number: a positive integer to be converted into a roman numeral.
                Will use integer part if passed a float.

    Returns:
        The string representation of number.

    Examples:
        >>> int_to_roman_string(5)
        'V'
        >>> int_to_roman_string(2019)
        'MMXIX'

    Raises:
        ValueError: if passed a negative number
    """
    number = int(number)
    if number < 0:
        raise ValueError(f"""{number} is negative, cannot convert to Roman
                         numeral""")
    result = ''
    for symbol, value in _ROMAN_SYMBOLS:
        result += (number//value) * symbol
        number = number % value
    return result

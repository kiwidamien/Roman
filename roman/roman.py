from collections import namedtuple

RomanSymbol = namedtuple('RomanSymbol', 'value symbol')
RomanSymbols = [
    RomanSymbol(value=1000, symbol='M'), RomanSymbol(value=900, symbol='CM'),
    RomanSymbol(value=500, symbol='D'), RomanSymbol(value=400, symbol='CD'),
    RomanSymbol(value=100, symbol='C'), RomanSymbol(value=90, symbol='XC'),
    RomanSymbol(value=50, symbol='L'), RomanSymbol(value=40, symbol='XL'),
    RomanSymbol(value=10, symbol='X'), RomanSymbol(value=9, symbol='IX'),
    RomanSymbol(value=5, symbol='V'), RomanSymbol(value=4, symbol='IV'),
    RomanSymbol(value=1, symbol='I')
]

REPLACE = {}

SYMBOL_GROUPS = [('I', 'V', 'X'),
                 ('X', 'L', 'C'),
                 ('C', 'D', 'M')]
for unit, mid, upper in SYMBOL_GROUPS:
    REPLACE[unit*5] = mid
    REPLACE[unit*4] = unit + mid
    REPLACE[mid*2] = upper
    REPLACE[f'{mid}{unit}{mid}'] = unit + upper


def validate_string(numeral_string):
    valid_chars = 'IVXLCDM'
    illegal_chars = [c for c in numeral_string if c not in valid_chars]
    if illegal_chars:
        raise ValueError(f'''Characters {set(illegal_chars)} found in numeral
                         string, only allowed {valid_chars}''')
    for reducible_substring in REPLACE:
        if reducible_substring in numeral_string:
            raise ValueError(f'''{reducible_substring} in {numeral_string} could
                             be replaced with {REPLACE[reducible_substring]}''')

def roman_string_to_int(numeral_string):
    """
    Converts a Roman numeral string to integer form
    """
    validate_string(numeral_string)
    total = 0
    for currentSymbol in RomanSymbols:
        while numeral_string.startswith(currentSymbol.symbol):
            total += currentSymbol.value
            numeral_string = numeral_string[len(currentSymbol.symbol):]
    return total

# Example take from https://www.youtube.com/watch?v=nrVIlhtoE3Y&t=40m18s
def int_to_roman_string2(number):
    roman_string = number * 'I'
    for reducible_substring in REPLACE:
        roman_string = roman_string.replace(reducible_substring)
    return roman_string

def int_to_roman_string(number):
    result = ''
    for currentSymbol in RomanSymbols:
        result += (number//currentSymbol.value) * currentSymbol.symbol
        number = number % currentSymbol.value
    return result

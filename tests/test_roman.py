import pytest
from roman.roman import int_to_roman_string, roman_string_to_int

def test_empty_string_gives_zero():
    assert roman_string_to_int('') == 0

def test_error_on_lower_case():
    with pytest.raises(ValueError, message="Error with lower case numerals"):
        roman_string_to_int('iii')

def test_III_is_converted_to_3():
    assert roman_string_to_int('III') == 3

def test_IV_is_romaned_to_four():
    assert roman_string_to_int('IV') == 4

def test_LLL_throws_ValueError():
    with pytest.raises(ValueError, message="Reducible numerals are not allowed"):
        roman_string_to_int('LLL')

def test_CCC_gives_300():
    assert roman_string_to_int('CCC') == 300

def test_CI_allows_and_gives_101():
    assert roman_string_to_int('CI') == 101

def test_IC_throws_ValueError():
    with pytest.raises(ValueError, message="""Filtering bad orderings of legal
                       characters failed"""):
        roman_string_to_int('IC')

def test_5_gives_V():
    assert int_to_roman_string(5) == 'V'

def test_10_gives_X():
    assert int_to_roman_string(10) == 'X'

def test_50_gives_L():
    assert int_to_roman_string(50) == 'L'

def test_100_gives_C():
    assert int_to_roman_string(100) == 'C'

def test_500_gives_D():
    assert int_to_roman_string(500) == 'D'

def test_1000_gives_M():
    assert int_to_roman_string(1000) == 'M'

def test_6000_is_MMMMMM():
    assert int_to_roman_string(6000) == 'MMMMMM'

def test_2018_is_MMXVIII():
    assert int_to_roman_string(2018) == 'MMXVIII'

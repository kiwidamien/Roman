import unittest
import roman.roman

class RomanNumeralTest(unittest.TestCase):
    def test_empty_string_gives_zero(self):
        self.assertEqual(roman.roman_string_to_int(''), 0)

    def test_error_on_lower_case(self):
        with self.assertRaises(ValueError):
            roman.roman_string_to_int('iii')

    def test_III_is_romaned_to_three(self):
        self.assertEqual(roman.roman_string_to_int('III'), 3)

    def test_IV_is_romaned_to_four(self):
        self.assertEqual(roman.roman_string_to_int('IV'), 4)

    def test_LLL_throws_ValueError(self):
        with self.assertRaises(ValueError):
            roman.roman_string_to_int('LLL')

    def test_CCC_gives_300(self):
        self.assertEqual(roman.roman_string_to_int('CCC'), 300)

    def test_CI_allows_and_gives_101(self):
        self.assertEqual(roman.roman_string_to_int('CI'), 101)

    def test_IC_throws_ValueError(self):
        with self.assertRaises(ValueError):
            roman.roman_string_to_int('IC')

    def test_5_gives_V(self):
        self.assertEqual(roman.int_to_roman_string(5), 'V')

    def test_10_gives_X(self):
        self.assertEqual(roman.int_to_roman_string(10), 'X')

    def test_50_gives_L(self):
        self.assertEqual(roman.int_to_roman_string(50), 'L')

    def test_100_gives_C(self):
        self.assertEqual(roman.int_to_roman_string(100), 'C')

    def test_500_gives_D(self):
        self.assertEqual(roman.int_to_roman_string(500), 'D')

    def test_1000_gives_M(self):
        self.assertEqual(roman.int_to_roman_string(1000), 'M')

    def test_6000_is_MMMMMM(self):
        self.assertEqual(roman.int_to_roman_string(6000), 'MMMMMM')

    def test_2018_is_MMXVIII(self):
        self.assertEqual(roman.int_to_roman_string(2018), 'MMXVIII')

if __name__ == '__main__':
    unittest.main()

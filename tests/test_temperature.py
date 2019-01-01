import pytest

from roman.temperature import convert, convert_all

def test_0_K_is_neg_273_pt_15_C():
    assert convert_all(0, 'K')['C'] == -273.15
    assert convert(0, 'K', 'C') == -273.15

def test_100_C_is_212_F():
    assert convert_all(100,'C')['F'] == 212
    assert convert(100, 'C', 'F') == 212

def test_0_C_is_32_F():
    assert convert_all(0, 'C')['F'] == 32
    assert convert(0, 'C', 'F') == 32

def test_0_C_is_273_15_K():
    assert convert_all(0, 'C')['K'] == 273.15
    assert convert(0, 'C', 'K') == 273.15

def test_negative_temp_in_K_gives_error():
    with pytest.raises(ValueError, message="Expecting Value Error"):
        convert_all(-100, 'K')

def test_negative_temp_in_K_okay_with_flag_set():
    convert_all(-100, 'K', True)

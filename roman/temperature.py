UNITS = 'KFC'
UNIT_NAMES = {
    'Kelvin': 'K',
    'Fahrenheit': 'F',
    'Celsius': 'C',
    'Centigrade': 'C',
}

ABSOLUTE_ZERO_IN_C = -273.15


def convert_C_to_K(tempC):
    return tempC - ABSOLUTE_ZERO_IN_C


def convert_K_to_C(tempK):
    return tempK + ABSOLUTE_ZERO_IN_C


def convert_C_to_F(tempC):
    return 9*tempC/5 + 32


def convert_F_to_C(tempF):
    return 5*(tempF - 32)/9


def convert_K_to_F(tempK):
    tempC = convert_K_to_C(tempK)
    return convert_C_to_F(tempC)


def convert_F_to_K(tempF):
    tempC = convert_F_to_C(tempF)
    return convert_C_to_K(tempC)


CONVERSIONS = {
    ('K', 'K'): lambda x: x,
    ('K', 'F'): convert_K_to_F,
    ('K', 'C'): convert_K_to_C,
    ('F', 'K'): convert_F_to_K,
    ('F', 'F'): lambda x: x,
    ('F', 'C'): convert_F_to_C,
    ('C', 'K'): convert_C_to_K,
    ('C', 'F'): convert_C_to_F,
    ('C', 'C'): lambda x: x
}


def convert_all(temp, unit):
    """Returns a dictionary, converting temp in 'unit' to all different
    units"""
    return {new_unit: CONVERSIONS[(unit, new_unit)](temp) for new_unit in
            UNITS}

def convert(temp, from_unit, to_unit):
    """Converts temp in unit from_unit to to_unit"""
    return _CONVERSIONS[(from_unit, to_unit)](temp)

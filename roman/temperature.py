UNITS = 'KFC'
UNIT_NAMES = {
    'Kelvin': 'K',
    'Fahrenheit': 'F',
    'Celsius': 'C',
    'Centigrade': 'C',
}

ABSOLUTE_ZERO_IN_C = -273.15


def _convert_C_to_K(tempC):
    return tempC - ABSOLUTE_ZERO_IN_C


def _convert_K_to_C(tempK):
    return tempK + ABSOLUTE_ZERO_IN_C


def _convert_C_to_F(tempC):
    return 9*tempC/5 + 32


def _convert_F_to_C(tempF):
    return 5*(tempF - 32)/9


def _convert_K_to_F(tempK):
    tempC = _convert_K_to_C(tempK)
    return _convert_C_to_F(tempC)


def _convert_F_to_K(tempF):
    tempC = _convert_F_to_C(tempF)
    return _convert_C_to_K(tempC)


_CONVERSIONS = {
    ('K', 'K'): lambda x: x,
    ('K', 'F'): _convert_K_to_F,
    ('K', 'C'): _convert_K_to_C,
    ('F', 'K'): _convert_F_to_K,
    ('F', 'F'): lambda x: x,
    ('F', 'C'): _convert_F_to_C,
    ('C', 'K'): _convert_C_to_K,
    ('C', 'F'): _convert_C_to_F,
    ('C', 'C'): lambda x: x
}


def convert_all(temp, unit, allow_neg_abs=False):
    """Converts temp expressed in unit to Kelvin, Fahrenheit, and Celsius
    Args:
        temp (numeric): the numeric value of the temperature.
        unit (string): one of 'K', 'F', or 'C' to express if temp is given in
                       Kelvin, Farenheit, or Celsius respectively.
        allow_neg_abs: set to True to allow temperatures below absolute zero.
    Returns:
        A dictionary with keys representing the unit, and values representing
        the temperature in that unit.
    Examples:
        >>> convert_all(0, 'C')
        {'K': 273.15, 'F': 32.0, 'C': 0}
        >>> convert_all(212, 'F')
        {'K': 373.15, 'F': 212, 'C': 100}
    Raises:
        KeyError: If unit is not one of 'K', 'F', or 'C'
        ValueError: If the temperature is below absolute zero, and
                    allow_neg_abs is False
    """
    values = {new_unit: _CONVERSIONS[(unit, new_unit)](temp) for new_unit in
              UNITS}
    if (not allow_neg_abs) and values['K'] < 0:
        raise ValueError("""{temp} {unit} is a negative temperature on the \
                         Kelvin scale ({values['K']} K). If you want to do \
                         this conversion, set allow_neg_abs to True""")
    return values


def convert(temp, from_unit, to_unit):
    """Converts temp expressed in from_unit to the numeric value expressed in
    to_unit.
    Args:
        temp (numeric): the numeric value of the temperature in from_unit.
        from_unit (string): one of 'K', 'F', or 'C' to express if temp is given
                            in Kelvin, Farenheit, or Celsius respectively.
        to_unit (string): one of 'K', 'F', or 'C' to express the unit to
                          convert the temperature in to.
    Returns:
        The numeric value of the temperature in to_unit
    Examples:
        # convert 0C into F
        >>> convert(0, 'C', 'F')
        32
        # convert 0F into C
        >>> convert(0, 'F', 'C')
        -17.777777778
        # there is one temp where C and F have same numeric value
        >>> convert(-40, 'F', 'C')
        -40
    Raises:
        KeyError: If either from_unit or to_unit are not 'K', 'F', or 'C'
    """
    return _CONVERSIONS[(from_unit, to_unit)](temp)

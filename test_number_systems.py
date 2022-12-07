"""Unit test for the number system converter function."""
from number_systems import number_system_converter
import pytest

def test_number_system_converter():
    # x > 0
    assert number_system_converter(5) == 'Binary: 0b101, hexadecimal: 0x5, octal: 0o5'
    assert number_system_converter(1) == 'Binary: 0b1, hexadecimal: 0x1, octal: 0o1'
    assert number_system_converter(420) == 'Binary: 0b110100100, hexadecimal: 0x1a4, octal: 0o644'
    assert number_system_converter(123456789) == 'Binary: 0b111010110111100110100010101, hexadecimal: 0x75bcd15, octal: 0o726746425'
    # x <= 0
    with pytest.raises(ValueError):
        number_system_converter(0)
    with pytest.raises(ValueError):
        number_system_converter(-1)
    with pytest.raises(ValueError):
        number_system_converter(-69)
    # return TypeError in other cases
    with pytest.raises(TypeError):
        number_system_converter(True)
    with pytest.raises(TypeError):
        number_system_converter(3 + 3j)
    with pytest.raises(TypeError):
        number_system_converter("string")
    with pytest.raises(TypeError):
        number_system_converter(111.11)
    with pytest.raises(TypeError):
        number_system_converter(3.5)
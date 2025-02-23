import pytest
from src.area import calculate_area_square

def test_calculate_area_square_valid():
    result = calculate_area_square(49)  # Input is correct
    expected_output = 2500  # Incorrect expected value to force failure
    assert result == expected_output, f"Expected {expected_output}, got {result}"

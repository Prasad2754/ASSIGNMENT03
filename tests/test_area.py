import pytest
import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Correct import
from area import calculate_area_square  # Ensure import works

# Ensure function starts with 'test_'
def test_calculate_area_square():
    result = calculate_area_square(4)
    assert result == 16, f"Expected 16, got {result}"

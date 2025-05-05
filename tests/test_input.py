import pytest
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from process_inputs import *


# valid inputs
@pytest.mark.parametrize("input, expected", [
    ("abcdefg", True), 
    ("Guinea-Bissau", True),
    ("Canada", True), 
    ("United States", True),
    ("Brazil", True)
])
def test_valid_input(input, expected): 
    assert(validate_user_input(input) == expected)

# invalid inputs
@pytest.mark.parametrize("input, expected", [
    ("!@#$as4", False), 
    ("C@nada", False), 
    ("America!", False), 
    ("1234", False), 
    ("", False)
])
def test_invalid_inputs(input, expected): 
    assert(validate_user_input(input) == expected)

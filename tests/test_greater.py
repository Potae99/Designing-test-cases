"""Test cases for the greater function."""



#Standard library


#3rd party library
import pytest

#Project library
from utility.comparison import greater

#--------------------------------------------------------------------------------------
@pytest.mark.parametrize(
    "num_1, num_2, expected",
    [
        (7, 5, 7),          #Case 1: num_1 > num_2
        (100, 200, 200),    #Case 2: num_2 > num_1
        (-5, -5, -5),       #Case 3:num_1 == num_2

    ]
)

def test_greater(num_1, num_2, expected):
    """Get the greater number between num_1 and num_2."""
    # Arrange
    # Act

    result = greater(num_1, num_2)

    # Assert
    assert result == expected
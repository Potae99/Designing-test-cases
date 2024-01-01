"""Test cases for the min function."""



#Standard library


#3rd party library
import pytest

#Project library
from utility.comparison import miner

#--------------------------------------------------------------------------------------
@pytest.mark.parametrize(
    "num_1, num_2, expected",
    [
        (5, 7, 5),          #Case 1: num_1 < num_2
        (200, 100, 100),    #Case 2: num_2 < num_1
        (-5, -5, -5),       #Case 3:num_1 == num_2

    ]
)

def test_min(num_1, num_2, expected):
    """Get the greater number between num_1 and num_2."""
    # Arrange
    # Act

    result = min(num_1, num_2)

    # Assert
    assert result == expected
"""
Unit regression test for the measure module
"""

import molecool
import numpy as np
import pytest

def test_calculate_distance():
    """Test that calculate_distance function calculates what we expect"""

    r1 = np.array([0, 0, 0])
    r2 = np.array([0, 1, 0])

    expected_distance = 1.0
    calculated_distance = molecool.calculate_distance(r1, r2)

    # NOTE: If these are floats, make sure to use approximately equals
    assert expected_distance == calculated_distance
  

@pytest.mark.parametrize(
        "p1, p2, expected_distance",
        [
            (np.array([0.0, 0.0, 0.0]), np.array([0.0, 0.0, 1.0]), 1.0),
            (np.array([0.0, 0.0, 0.0]), np.array([0.0, 0.0, 5.0]), 5.0),
            (np.array([0.0, 0.0, 0.0]), np.array([0.0, 0.0, 20.0]), 20.0)
        ]
)
def test_calculate_distance_many(p1, p2, expected_distance):
    
    calculated_distance = molecool.calculate_distance(p1, p2)
    assert np.isclose(calculated_distance, expected_distance, rtol=1e-2)
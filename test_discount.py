
from oop import validate_age
import pytest

# @pytest.mark.parametrize(
#         "price,discount,expected",
#         [(0, 10, "Invalid price"),
#            (-100, 10,"Invalid price"),
#             (1000, -5,"Invalid discount"),
#             (1000, 101,"Invalid discount")
#         ]
# )
# def test_discount_edge_cases(price, discount, expected):
#     assert calculate_discount(price, discount) == expected


def test_valid_age():
    assert validate_age(25) == "Valid age"
def test_negative_age():
    with pytest.raises(ValueError, match="Age cannot be negative"):
        validate_age(-5)
def test_invalid_age():
    with pytest.raises(ValueError,match="Invalid age"):
        validate_age(200)

# def test_full_discount():
#     assert calculate_discount("1000","100")==0.0

# def test_invalid_discount():
#     assert calculate_discount(1000, 150) == "Invalid discount"


# def test_invalid_input():
#     assert calculate_discount(None, 10) == "Invalid input"

"""Test some functions."""
from pytest import approx

from myproject.some import double_float, wide_num_to_float


def test_double_float():
    """Test double_float."""
    assert double_float(2) == 4.0


def test_wide_num_to_float():
    """Test wide_num_to_float."""
    # approx を使うと、誤差の範囲を指定できます。
    assert wide_num_to_float("１２３４５") == approx(12345.0, rel=1e-6)
    assert wide_num_to_float("１．４１４２１４") == approx(1.414214, rel=1e-6)
    assert wide_num_to_float("四三二一零") == approx(43210, rel=1e-4)


# def test_double_float_fail():
#     assert double_float(2) == 5.0

from division_func import division
import pytest

@pytest.mark.parametrize("a, b, exp_result", [(14, 7, 2),
                                              (20, 10, 2),
                                              (15, 5, 3),
                                              (10, -2, -5),
                                              (5, 2.5, 2)])
def test_division_work(a, b, exp_result):
    assert division(a, b) == exp_result

@pytest.mark.parametrize("expected_expection, divider, div", [(ZeroDivisionError, 0, 10),
                                                         (TypeError, "2", 20)])
def test_division_w_error(expected_expection, divider, div):
    with pytest.raises(expected_expection):
        division(div, divider)




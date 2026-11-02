import pytest

from ordering import calculate_order_total


@pytest.mark.parametrize(
    "subtotal, discount, expected",
    [
        (500, 10, 450.0),    # normal discount
        (199.99, 25, 149.99),  # normal discount, decimal subtotal
        (500, 0, 500.0),     # zero discount
        (0, 50, 0.0),        # zero subtotal
        (500, 100, 0.0),     # boundary: max discount
        (0.01, 1, 0.01),     # boundary: tiny values
    ],
)
def test_valid_order_totals(subtotal, discount, expected):
    assert calculate_order_total(subtotal, discount) == expected


@pytest.mark.parametrize(
    "subtotal, discount",
    [
        (500, -1),     # invalid: negative discount (just below boundary)
        (500, 100.1),  # invalid: just above boundary
        (500, 150),    # invalid: discount over 100
        (-10, 10),     # invalid: negative subtotal
    ],
)
def test_invalid_values_raise_value_error(subtotal, discount):
    with pytest.raises(ValueError):
        calculate_order_total(subtotal, discount)


@pytest.mark.parametrize("subtotal, discount", [("500", 10), (500, "ten"), (None, 0)])
def test_invalid_types_raise_type_error(subtotal, discount):
    with pytest.raises(TypeError):
        calculate_order_total(subtotal, discount)

import pytest


def add(a, b):
    a = float(a)
    b = float(b)
    return a + b

def test_add_positive_integers():
    assert add(2, 3) == 5

def test_add_floats():
    # This is more robust than assert add(2.1, 3.1) == 5.2
    assert add(2.1, 3.1) == pytest.approx(5.2)

def test_add_with_invalid_string_raises_error():
    with pytest.raises(ValueError):
        add("hello", "world")
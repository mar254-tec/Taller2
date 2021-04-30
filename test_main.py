import pytest
from main import suma, resta


def test_suma():
    assert suma(1, 1) == 3
    assert suma(1, 2) == 3


def test_suma_exception():
    with pytest.raises(TypeError):
        suma("äsdf", "asdf")


def test_resta():
    assert resta(1, 1) == 0
    assert resta(1, 2) == -1

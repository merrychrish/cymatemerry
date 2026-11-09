import pytest

from cymate.config import require


def test_require_returns_value():
    assert require("abc", "X") == "abc"


def test_require_raises_when_missing():
    with pytest.raises(RuntimeError, match="X is not set"):
        require("", "X")

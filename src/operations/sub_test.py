import pytest
from .sub import SubOperation

subOperation = SubOperation()

@pytest.mark.parametrize('num1, num2, result',
    [
        (3, 2, 1),
        (4, 1, 3)
    ]
)
def test_sub(num1, num2, result):
    assert subOperation.diferenca(num1, num2) == result

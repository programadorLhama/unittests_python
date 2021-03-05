from faker import Faker
from .operations.test.add import AddOperationSpy
from .operations.test.sub import SubOperationSpy
from .calculadora import Calculadora

fake = Faker()

def test_add():
    addOperation = AddOperationSpy()
    subOperation = SubOperationSpy()
    calculadora = Calculadora(addOperation, subOperation)

    number1 = fake.random_number()
    number2 = fake.random_number()

    result = calculadora.add(number1, number2, True)

    # Testing input
    assert addOperation.soma_attributes['number1'] == number1
    assert addOperation.soma_attributes['number2'] == number2

    # Testing output
    assert result is not None


def test_sub():
    addOperation = AddOperationSpy()
    subOperation = SubOperationSpy()
    calculadora = Calculadora(addOperation, subOperation)

    number1 = fake.random_number()
    number2 = fake.random_number()

    result = calculadora.sub(number1, number2, True)

    # Testing input
    assert subOperation.diferenca_attributes['number1'] == number1
    assert subOperation.diferenca_attributes['number2'] == number2

    # Testing output
    assert result is not None

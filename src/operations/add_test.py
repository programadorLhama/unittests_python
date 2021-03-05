from faker import Faker
from .add import AddOperation

fake = Faker()

def test_soma():
    addOperation = AddOperation()

    number1 = fake.random_number()
    number2 = fake.random_number()
    expected = number1 + number2

    result = addOperation.soma(number1, number2)

    assert result == expected
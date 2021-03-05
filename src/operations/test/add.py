from faker import Faker

faker = Faker()

class AddOperationSpy:

    def __init__(self):
        self.soma_attributes = {}

    def soma(self, number1, number2):
        self.soma_attributes['number1'] = number1
        self.soma_attributes['number2'] = number2

        return faker.random_number()

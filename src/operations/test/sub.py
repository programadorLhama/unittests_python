from faker import Faker

faker = Faker()

class SubOperationSpy:

    def __init__(self):
        self.diferenca_attributes = {}

    def diferenca(self, number1, number2):
        self.diferenca_attributes['number1'] = number1
        self.diferenca_attributes['number2'] = number2

        return faker.random_number()

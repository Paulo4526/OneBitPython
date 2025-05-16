class Phone:
    def __init__(self, brand, model, model_name, price):
        self._brand = brand
        self._model = model
        self._model_name = model_name
        self._price = price

    def __str__(self):
        return f"\n{self._brand} \n{self._model} \n{self._model_name} \n{self._price}R$\n"

    @staticmethod
    def make_a_call(phone_number):
        print(f"Ligando para {phone_number}")
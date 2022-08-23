from abc import ABC


class CurrencyConvert(ABC):
    def convert(self, from_currency, to_currency, amount) -> float:
        pass


class FxConverter(CurrencyConvert):
    def convert(self, from_currency, to_currency, amount) -> float:
        print('Converting currency using Fx Api')
        print(f'{amount} {from_currency}: {amount * 1.2} {to_currency}')
        return amount * 2


class App:
    def __init__(self, converter: CurrencyConvert):
        self._converter = converter

    def start(self):
        self._converter.convert('EUR', 'USD', 100)


if __name__ == '__main__':
    converter = FxConverter()
    app = App(converter)
    app.start()

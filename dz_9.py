import requests
from bs4 import BeautifulSoup

class CurrencyConverter:
    def __init__(self):
        self.exchange_rates = {}

    def fetch_exchange_rates(self):
        url = "https://bank.gov.ua/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

    def convert_to_usd(self, amount, currency):
        if currency.upper() in self.exchange_rates:
            return amount / self.exchange_rates[currency.upper()]
        else:
            return "Курс валюти не знайдено."

if __name__ == "__main__":
    converter = CurrencyConverter()
    converter.fetch_exchange_rates()
    amount = float(input("Введіть суму в вашій валюті: "))
    currency = input("Введіть код вашої валюти наприклад, USD, EUR, UAH: ")
    result = converter.convert_to_usd(amount, currency)
    print("Відповідна сума в доларах США:", result)

import requests


def main():
    base = input(f'Input currency to convert from:\n'
                 f'1: EUR, 2: USD, 3: RUB\n')
    match base:
        case '1': base = "EUR"
        case '2': base = "USD"
        case '3': base = "RUB"
    rate = input(f'Input currency to convert into:\n'
                 f'1: EUR, 2: USD, 3: RUB\n')
    match rate:
        case '1': rate = "EUR"
        case '2': rate = "USD"
        case '3': rate = "RUB"
    url = f"https://api.apilayer.com/fixer/latest?base={base}&symbols={rate}&apikey=BAvGlFFYWfKr5HynX6HpLXK0qt4us5Hw"
    res = requests.get(url)
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccesful!")
    data = res.json()
    currency_rate = data["rates"][rate]
    amount = input(
        f'Input how much {base} '
        f'would you like to convert into {rate}: '
    )
    converted_currency = round((float(currency_rate) * float(amount)), 2)
    print(f'1 {base} equals {currency_rate} {rate}')
    print(f'{amount} {base} equals {converted_currency} {rate}')


if __name__ == "__main__":
    main()

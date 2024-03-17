import requests
# from flask import Flask, render_template, request, redirect, abort, url_for


def main():
    base = input(f'Input currency to compare to:\n'
                 f'1: EUR, 2: USD, 3: RUB\n')
    match base:
        case '1': base = "EUR"
        case '2': base = "USD"
        case '3': base = "RUB"
    rate = input(f'Input currency to compare:\n'
                 f'1: EUR, 2: USD, 3: RUB\n')
    match rate:
        case '1': rate = "EUR"
        case '2': rate = "USD"
        case '3': rate = "RUB"
    url = "https://api.apilayer.com/fixer/latest?base={}&symbols={}&apikey=BAvGlFFYWfKr5HynX6HpLXK0qt4us5Hw".format(base, rate)
    res = requests.get(url)
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccesful!")
    data = res.json()
    print(url)
    # currency_base = data["base"]
    currency_rate = data["rates"][rate]
    print(res.status_code)
    print(f'1 {base} equals {currency_rate} {rate}')


if __name__ == "__main__":
    main()

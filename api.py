import requests


def main():
    res = requests.get("https://api.apilayer.com/fixer/latest?base=USD&symbols={}&apikey=BAvGlFFYWfKr5HynX6HpLXK0qt4us5Hw")
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccesful!")  
    data = res.json()
    currency_base = data["base"]
    currency_rate = data["rates"]["RUB"]
    print(data, '\n', res.status_code)


if __name__ == "__main__":
    main()

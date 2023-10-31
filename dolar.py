import requests, json
from os import system

dol = int(input('Insira o valor em dólar que queira migrar para real: '))
req = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')

data = req.json()

cotacao = float(data['USDBRL']['bid'])
calc = dol * cotacao

if __name__ == '__main__':
    system('cls')

    print(f'O valor de {dol} USD é igual a {calc:.2f} BRL.')


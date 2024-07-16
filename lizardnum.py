from time import sleep as delay
import signal
import sys
import os
import requests
import json
import re

import banner
import countrycodes

N = "\033[37;1m"
R = "\033[31;1m"
G = "\033[31;1m"
W = "\033[37;1m"
L = "\033[37;1m"

T = G + ' [' + W + '+' + G + ']' + W
U = G + ' [' + W + '*' + G + ']' + W
A = '\n' + G + ' [' + W + '!' + G + ']' + W
I = G + ' [' + W + '>' + G + ']' + W

#your apikey of NumVerify
apikey = ''

def signal_handler(sig, frame):
    print(f'\n\n{A} Saliendo...\n')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def numverify(number,country):
    agent = {'User-Agent':'Mozilla Firefox Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0'}

    print(f'\n{T} Scaning:{R} {country} {number}\n')

    pe = requests.get(
            'http://apilayer.net/api/validate?access_key={}&number={}&country_code={}&format=1'.format(apikey,number,country),
            headers=agent
            )
    data = json.loads(pe.text)

    return data

def lizardNumber():
    pattern = r'(\+\d+)\s+([\d\s\-\(\)]+)'

    while True:
        phone = input(f'{T} Example:{R} +9 999 999 999\n{I} Phone:{R} ')
        match = re.search(pattern, phone)

        if match:
            code = match.group(1)
            number = re.sub(r'[\s\-\(\)]', '', match.group(2))
            
            country_code = countrycodes.getCountryCode(code)

            if country_code:
                #print(f'Country code: {country_code}')
                #print(f'Number: {number}')
                break
            else:
                print(f'{A} Country code not found\n')
        else:
            print(f'{A} Invalid phone number format\n')

    clear()
    print(f'{L} {banner.lizard()}')
    
    data = numverify(number, country_code)

    if not data:
        print(f'{A} Error in Apykey\n')
        return

    with open('data.txt', 'a') as file:
        file.write(f'\n')

    for d in data:
        delay(.1)
        print(f'{U} {d}:{R} {data[d]}')
        with open('data.txt', 'a') as file:
            file.write(f'\n[*] {d}: {data[d]}')
    
    press = input(f'{A} Continue \'ENTER\'')

if __name__ == '__main__':
    while True:
        clear()
        print(f'{L} {banner.lizard()}')

        lizardNumber()

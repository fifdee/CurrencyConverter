import requests
import json

cache_rates = {}
my_cur = input().lower()


def get_rate(my_cur_code, sec_cur_code, initial=False):
    if not initial:
        print('Checking the cache...')
    if sec_cur_code in cache_rates:
        if not initial:
            print('Oh! It is in the cache!')
    else:
        if not initial:
            print('Sorry, but it is not in the cache!')
        if my_cur_code == sec_cur_code:
            cache_rates[sec_cur_code] = 1.0
        else:
            url = f'http://www.floatrates.com/daily/{my_cur_code}.json'
            r = requests.request('GET', url)
            data = json.loads(r.text)
            cache_rates[sec_cur_code] = data[sec_cur_code]['rate']

    return cache_rates[sec_cur_code]


get_rate(my_cur, 'usd', initial=True)
get_rate(my_cur, 'eur', initial=True)

while True:
    chosen_cur = input()
    if chosen_cur == '':
        break
    chosen_cur = chosen_cur.lower()
    my_amount = float(input().strip())

    print(f'You received {round(my_amount * get_rate(my_cur, chosen_cur), 2)} {chosen_cur.upper()}.')
import requests
import json


cash_api_url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
debet_api_url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11'
cash_res = json.loads(requests.get(cash_api_url).text)
debet_res = json.loads(requests.get(debet_api_url).text)


def ask_type():
    type_conv = input('Выберите CASH или DEBET?\n').upper()
    if type_conv != 'CASH' and type_conv != 'DEBET':
        print('Нужно ввести "CASH" или "DEBET"!')
        ask_type()
    else:
        ask_valute(type_conv)

def ask_valute(ty):
    if ty == 'CASH':
        available_vals = []
        print('VALUTES: ', end='')
        for i in cash_res:
            available_vals.append(i['ccy'])
            print(i['ccy'], end=' ')
        print()
        valute = input('Выберите валюту: ').upper()
        if valute in available_vals:
            ask_number(valute, ty)
        else:
            print('Выберите валюту из возможных!')
            ask_valute(ty)
    else:
        available_vals = []
        print('VALUTES: ', end='')
        for i in debet_res:
            available_vals.append(i['ccy'])
            print(i['ccy'], end = ' ')
        print()
        valute = input('Выберите валюту: ').upper()
        if valute in available_vals:
            ask_number(valute, ty)
        else:
            print('Выберите валюту из списка!')
            ask_valute(ty)

def ask_number(vals, ty):
    if ty == 'CASH':
        for i in cash_res:
            if i['ccy'] == vals:
                print('Покупка ' + i['buy'] + ' ' + i['base_ccy'])
                print('Продажа ' + i['sale'] + ' ' + i['base_ccy'])
                buy_sale = input('Вы хотите купить(BUY) или продать(SALE)?\n').upper()
                if buy_sale == 'BUY':
                    number_vals = input('Введите количество, которое хотите купить: ')
                    try:
                        number_vals = float(number_vals)
                    except Exception:
                        print('Вы обязаны ввести число!')
                        ask_number(vals, ty)
                    print('Стоимость: ' + str(round(float(i['buy']) * number_vals, 2)) + ' ' + i['base_ccy'] )
                    break
                elif buy_sale == 'SALE':
                    number_vals = input('Введите количество, которое хотите продать: ')
                    try:
                        number_vals = float(number_vals)
                    except Exception:
                        print('Вы обязаны ввести число!')
                        ask_number(vals, ty)
                    print('Стоимость: ' + str(round(float(i['sale']) * number_vals, 2)) + ' ' + i['base_ccy'])
                    break
                else:
                    print('Вы должны ввести "BUY" или "SALE"')
                    ask_number(vals, ty)
    else:
        for i in debet_res:
            if i['ccy'] == vals:
                print('Покупка ' + i['buy'] + ' ' + i['base_ccy'])
                print('Продажа ' + i['sale'] + ' ' + i['base_ccy'])
                buy_sale = input('Вы хотите купить(BUY) или продать(SALE)?\n').upper()
                if buy_sale == 'BUY':
                    number_vals = input('Введите количество, которое хотите купить: ')
                    try:
                        number_vals = float(number_vals)
                    except Exception:
                        print('Вы обязаны ввести число!')
                        ask_number(vals, ty)
                    print('Стоимость: ' + str(round(float(i['buy']) * number_vals, 2)) + ' ' + i['base_ccy'])
                    break
                elif buy_sale == 'SALE':
                    number_vals = input('Введите количество, которое хотите продать: ')
                    try:
                        number_vals = float(number_vals)
                    except Exception:
                        print('Вы обязаны ввести число!')
                        ask_number(vals, ty)
                    print('Стоимость: ' + str(round(float(i['sale']) * number_vals, 2)) + ' ' + i['base_ccy'])
                    break
                else:
                    print('Вы должны ввести "BUY" или "SALE"')
                    ask_number(vals, ty)


if __name__ == '__main__':
    ask_type()
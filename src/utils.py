import json
import os
from datetime import datetime


def list_of_dates(all_operations):
    """Функция возвращает список из пяти дат от последних
    успешных операций
    из json файла"""
    catalog = []
    for i in range(len(all_operations)):
        if all_operations[i] != {} and all_operations[i]['state'] != "CANCELED":
            catalog.append(all_operations[i]['date'])
    sorted_catalog = sorted(catalog)
    last_five_catalog = sorted_catalog[-5:]
    return last_five_catalog


def get_date(dictionary):
    """Функция возвращает имя ключа для дальнейшей сортировки по нему"""
    return dictionary['date']


def list_of_operations(all_operations, catalog):
    """Функция возвращает список из словарей с информацией по последним
пяти успешным операциям"""
    catalog_ops = []
    for i in range(len(all_operations)):
        for a in range(len(catalog)):
            if all_operations[i] == {}:
                continue
            if all_operations[i]['state'] == "CANCELED":
                continue
            if all_operations[i]['date'] == catalog[a]:
                catalog_ops.append(all_operations[i])
    catalog_ops_sorted = sorted(catalog_ops, key=get_date)
    catalog_ops_reverse = catalog_ops_sorted[::-1]
    return catalog_ops_reverse


def convert_number(number):
    """Функция скрывает часть номера счета или карты для вывода на экран"""
    if 'Счет' in number:
        return number[:5] + ' **' + number[-4:]
    else:
        return number[:-16] + number[-16:-12] + ' ' + number[-12:-10] + '** **** ' + number[-4:]


def print_operations(elem_of_list_ops):
    """Функция выводит 5 последних успешных операций из файла json"""
    thedate = datetime.fromisoformat(elem_of_list_ops['date'])
    description = elem_of_list_ops['description']
    from_whom = None
    if 'from' in elem_of_list_ops:
        from_whom = convert_number(elem_of_list_ops['from']) + ' -> '
    else:
        from_whom = ''
    to_whom = convert_number(elem_of_list_ops['to'])
    currency = elem_of_list_ops["operationAmount"]["currency"]["name"]
    amount = elem_of_list_ops["operationAmount"]["amount"]
    return f"""{thedate.strftime("%d.%m.%Y")} {description}
{from_whom}{to_whom}
{amount} {currency}
"""


def open_json_file(file_dir, file_name):
    operation_path = os.path.join(os.path.dirname(file_dir), file_name)
    with open(operation_path, 'r', encoding='utf-8') as file:
        ops_catalog = json.load(file)
    return ops_catalog

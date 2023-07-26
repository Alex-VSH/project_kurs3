import json
import os
from datetime import datetime


def open_json_file(file_dir, file_name):
    operation_path = os.path.join(os.path.dirname(file_dir), file_name)
    with open(operation_path, 'r', encoding='utf-8') as file:
        ops_catalog = json.load(file)
    return ops_catalog


def _get_date(dictionary):
    """Функция возвращает имя ключа для дальнейшей сортировки по нему"""
    return dictionary['date']


def get_list_of_5_succ_ops(all_operations):
    """Функция возвращает список из словарей с информацией по последним
пяти успешным операциям"""
    succ_ops = []
    for op in all_operations:
        if op.get('state') == "EXECUTED":
            succ_ops.append(op)
    sorted_ops = sorted(succ_ops, key=_get_date)
    return sorted_ops[-5:]


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


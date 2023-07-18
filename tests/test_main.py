import json
import os
import pytest

from src.utils import list_of_dates, list_of_operations, print_operations, get_date, convert_number, open_json_file


@pytest.fixture()
def load_json():
    operation_path = os.path.join(os.path.dirname(__file__), "operations_for_test.json")
    with open(operation_path, 'r', encoding='utf-8') as file:
        ops_catalog = json.load(file)
    return ops_catalog


def test_list_of_dates(load_json):
    assert list_of_dates(load_json) == ['2019-04-04T23:20:05.206878',
                                        '2019-07-03T18:35:29.512364',
                                        '2019-07-12T20:41:47.882230',
                                        '2019-08-26T10:50:58.294041',
                                        '2019-12-08T22:46:21.935582']


def test_get_date(load_json):
    assert get_date(load_json[0]) == '2019-08-26T10:50:58.294041'


def test_list_of_operations(load_json):
    assert list_of_operations(load_json, list_of_dates(load_json)) == [{'date': '2019-12-08T22:46:21.935582',
                                                                        'description': 'Открытие вклада',
                                                                        'id': 863064926,
                                                                        'operationAmount': {'amount': '41096.24',
                                                                                            'currency': {'code': 'USD',
                                                                                                         'name': 'USD'}},
                                                                        'state': 'EXECUTED',
                                                                        'to': 'Счет 90424923579946435907'},
                                                                       {'date': '2019-08-26T10:50:58.294041',
                                                                        'description': 'Перевод организации',
                                                                        'from': 'Maestro 1596837868705199',
                                                                        'id': 441945886,
                                                                        'operationAmount': {'amount': '31957.58',
                                                                                            'currency': {'code': 'RUB',
                                                                                                         'name': 'руб.'}},
                                                                        'state': 'EXECUTED',
                                                                        'to': 'Счет 64686473678894779589'},
                                                                       {'date': '2019-07-12T20:41:47.882230',
                                                                        'description': 'Перевод организации',
                                                                        'from': 'Счет 48894435694657014368',
                                                                        'id': 522357576,
                                                                        'operationAmount': {'amount': '51463.70',
                                                                                            'currency': {'code': 'USD',
                                                                                                         'name': 'USD'}},
                                                                        'state': 'EXECUTED',
                                                                        'to': 'Счет 38976430693692818358'},
                                                                       {'date': '2019-07-03T18:35:29.512364',
                                                                        'description': 'Перевод организации',
                                                                        'from': 'MasterCard 7158300734726758',
                                                                        'id': 41428829,
                                                                        'operationAmount': {'amount': '8221.37',
                                                                                            'currency': {'code': 'USD',
                                                                                                         'name': 'USD'}},
                                                                        'state': 'EXECUTED',
                                                                        'to': 'Счет 35383033474447895560'},
                                                                       {'date': '2019-04-04T23:20:05.206878',
                                                                        'description': 'Перевод со счета на счет',
                                                                        'from': 'Счет 19708645243227258542',
                                                                        'id': 142264268,
                                                                        'operationAmount': {'amount': '79114.93',
                                                                                            'currency': {'code': 'USD',
                                                                                                         'name': 'USD'}},
                                                                        'state': 'EXECUTED',
                                                                        'to': 'Счет 75651667383060284188'}]


def test_convert_number():
    assert convert_number("Счет 48894435694657014368") == 'Счет  **4368'
    assert convert_number("Maestro 1596837868705199") == 'Maestro 1596 83** **** 5199'
    assert convert_number("MasterCard 7158300734726758") == 'MasterCard 7158 30** **** 6758'
    assert convert_number("Visa Classic 6831982476737658") == 'Visa Classic 6831 98** **** 7658'
    assert convert_number("Visa Platinum 8990922113665229") == 'Visa Platinum 8990 92** **** 5229'


def test_print_operations(load_json):
    last_five_list = list_of_dates(load_json)
    list_ops_reverse = list_of_operations(load_json, last_five_list)
    assert print_operations(list_ops_reverse[0]) == '08.12.2019 Открытие вклада\nСчет  **5907\n41096.24 USD\n'
    assert print_operations(list_ops_reverse[1]) == ('26.08.2019 Перевод организации\n'
                                                     'Maestro 1596 83** **** 5199 -> Счет  **9589\n'
                                                     '31957.58 руб.\n')
    assert print_operations(list_ops_reverse[2]) == '12.07.2019 Перевод организации\nСчет  **4368 -> Счет  ' \
                                                    '**8358\n51463.70 USD\n'
    assert print_operations(list_ops_reverse[3]) == ('03.07.2019 Перевод организации\n'
                                                     'MasterCard 7158 30** **** 6758 -> Счет  **5560\n'
                                                     '8221.37 USD\n')


def test_open_json_file(load_json):
    assert open_json_file('tests', "operations_for_test.json") == load_json

import json
import os
import pytest

from src.utils import print_operations, _get_date, convert_number, open_json_file, get_list_of_5_succ_ops
from tests.data_for_test import test_data


@pytest.fixture()
def load_ops_for_test():
    operation_path = os.path.join(os.path.dirname(__file__), "operations_for_test.json")
    with open(operation_path, 'r', encoding='utf-8') as file:
        ops_catalog = json.load(file)
    return ops_catalog


def test__get_date(load_ops_for_test):
    assert _get_date(load_ops_for_test[0]) == '2019-08-26T10:50:58.294041'


def test_get_list_of_5_succ_ops(load_ops_for_test):
    assert get_list_of_5_succ_ops(load_ops_for_test) == test_data


conversion_pairs = [
    ("Счет 48894435694657014368", 'Счет  **4368'),
    ("Maestro 1596837868705199", 'Maestro 1596 83** **** 5199'),
    ("MasterCard 7158300734726758", 'MasterCard 7158 30** **** 6758'),
    ("Visa Classic 6831982476737658", 'Visa Classic 6831 98** **** 7658'),
    ("Visa Platinum 8990922113665229", 'Visa Platinum 8990 92** **** 5229'),
]


@pytest.mark.parametrize('before_masking, after_masking', conversion_pairs)
def test_convert_number(before_masking, after_masking):
    assert convert_number(before_masking) == after_masking


test_result = [
    (0, ('04.04.2019 Перевод со счета на счет\n'
                                                          'Счет  **8542 -> Счет  **4188\n'
                                                          '79114.93 USD\n')),
    (1, ('03.07.2019 Перевод организации\n'
                                                                              'MasterCard 7158 30** **** 6758 -> Счет  **5560\n'
                                                                              '8221.37 USD\n')),
    (2, '12.07.2019 Перевод организации\nСчет  **4368 -> Счет  ' \
                                                         '**8358\n51463.70 USD\n'),
    (3, ('26.08.2019 Перевод организации\n'
                                                                              'Maestro 1596 83** **** 5199 -> Счет  **9589\n'
                                                                              '31957.58 руб.\n'))

]
@pytest.mark.parametrize('index, result', test_result)
def test_print_operations(load_ops_for_test, index, result):
    assert print_operations(get_list_of_5_succ_ops(load_ops_for_test)[index]) == result



def test_open_json_file(load_ops_for_test):
    assert open_json_file('tests', "operations_for_test.json") == load_ops_for_test

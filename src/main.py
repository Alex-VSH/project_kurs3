import json
import os
from datetime import datetime
from utils import *


# Код программы
operation_path = os.path.join(os.path.dirname(__file__), "operations.json")


with open(operation_path, 'r', encoding='utf-8') as file:
    text = json.load(file)
    last_five_list = list_of_dates(text)
    list_ops_reverse = list_of_operations(text, last_five_list)
    for i in range(len(list_ops_reverse)):
        print(print_operations(list_ops_reverse[i]))

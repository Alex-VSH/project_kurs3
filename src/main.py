from utils import list_of_dates, list_of_operations, print_operations, open_json_file


# Код программы

ops_catalog = open_json_file('src', "operations.json")
last_five_list = list_of_dates(ops_catalog)
list_ops_reverse = list_of_operations(ops_catalog, last_five_list)
for i in range(len(list_ops_reverse)):
    print(print_operations(list_ops_reverse[i]))

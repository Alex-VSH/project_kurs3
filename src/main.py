from utils import get_list_of_5_succ_ops, print_operations, open_json_file


# Код программы

ops = open_json_file('src', "operations.json")
list_ops = get_list_of_5_succ_ops(ops)
for operation in list_ops:
    print(print_operations(operation))

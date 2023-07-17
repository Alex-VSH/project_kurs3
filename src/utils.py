from datetime import datetime


def list_of_dates(text):
    """Функция возвращает список из пяти дат от последних
    успешных операций
    из json файла"""
    list = []
    for i in range(len(text)):
        if text[i] == {}:
            continue
        if text[i]['state'] == "CANCELED":
            continue
        list.append(text[i]['date'])
    sorted_list = sorted(list)
    last_five_list = sorted_list[-5:]
    return last_five_list

def get_name(dictionary):
    """Функция возвращает имя ключа для дальнейшей сортировки по нему"""
    return dictionary['date']

def list_of_operations(text, list):
    """Функция возвращает список из словарей с информацией по последним
пяти успешным операциям"""
    list_ops = []
    for i in range(len(text)):
        for a in range(len(list)):
            if text[i] == {}:
                continue
            if text[i]['state'] == "CANCELED":
                continue
            if text[i]['date'] == list[a]:
                list_ops.append(text[i])
    list_ops_sorted = sorted(list_ops, key=get_name)
    list_ops_reverse = list_ops_sorted[::-1]
    return list_ops_reverse


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
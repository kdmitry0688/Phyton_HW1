
from import_phone import import_data
from export import export_data
from print_phone import print_data
from search import search_data


def input_data():
    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    phone_number = input("Введите телефон: ")
    note = input("Введите примечание: ")
    return [first_name, last_name, phone_number, note]


def choice_phone():
    print("Нажмите для импорта: 1, для экспорта: 2, для поиска: 3.")
    ch = input("Введите цифру: ")
    if ch == '1':
        import_data(input_data())
    elif ch == '2':
        data = export_data()
        print_data(data)
    else:
        word = input("Введите данные для поиска: ")
        data = export_data()
        item = search_data(word, data)
        if item != None:
            print("Имя".center(20), "Фамилия".center(20),
                  "Телефон".center(15), "Примечание".center(30))
            print("-"*85)
            print(item[0].center(20), item[1].center(20),
                  item[2].center(15), item[3].center(30))
        else:
            print("Данные не обнаружены")
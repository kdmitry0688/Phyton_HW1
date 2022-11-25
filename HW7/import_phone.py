
def import_data(data):
    sep = ';'
    with open('phone.csv', 'a', encoding='utf-8') as file:
        for i in data:
            file.write(f"{i}\n")
        file.write(f"\n")
        file.write(sep.join(data))
        file.write(f"\n")
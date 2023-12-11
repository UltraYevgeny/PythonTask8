import os

NAME_FILE = "Телефонный справочник.txt"

def main():
    """если есть файл, то его считать, если нет, то пустой список
    вывести меню и меню обработать в цикле"""
    data = {}
    # os.path.exists(NAME_FILE) - проверяет существует ли файл
    if os.path.exists(NAME_FILE):
        # with open(NAME_FILE) as f: - Открывает файл для чтения и он автоматически закрывается потом.
        with open(NAME_FILE) as f:
            # f.readlines() - читает строки по одной из файла
            # .split("\t") - разделение по табуляции
            for line in f.readlines():
                name, num = line.split("\t")
                data[name] = num
    else: 
        with open(NAME_FILE, "w") as f:
            pass

    while True: # выход из while только через break
        while True:
            print("1. Ввести данные")
            print("2. Поиск")
            print("3. Выход")
            user_choise = input("Введите: ")
            if user_choise not in ["1","2","3"]:
                print("Ошибка")
            else:
                break
        # match похожа на конструкцию if/else/elif, которая выполняет 
        # определенные действия в зависимости от некоторого условия. 
        # Однако функциональность match гораздо шире - она также позволяет 
        # извлечь данные из составных типов и применить действия к различным частям объектов.
        match user_choise:
            case '1':
                data = input_data(data)
            case '2':
                search_data(data)
            case '3':
                print('Выход')
                if not data:
                    return
                with open(NAME_FILE, "w") as f:
                    for name in data:
                        # file - ????
                        print(f"{name}\t{data[name]}", file=f)
                return


def input_data(data):
    name = input("Введите ФИО: ")
    # name.isalpha() - Проверяет, что строка состоит только из буквенных символов
    # Пробел это не буква. - хотели еще проверить: and name.isalpha() - Но ФИО через пробелы.
    if name and len(name.split()) == 3:
        num = input("Введите номер телефона: ")
        # Метод isdigit() возвращает True, если все символы в строке являются 
        # цифрами. Если нет, возвращается False.
        if num and num.isdigit():
            data[name.replace("\t", " ")] = num
            return data
    print("Не верный ввод данных")
    return data


def search_data(data):
    user_input = input("Ввести данные для поиска: ")
    while True:
            print("1. Искать фамилию")
            print("2. Найти имя")
            print("3. Найти отчество")
            print("4. Найти номер телефона")
            print("5. Вернуться в меню")
            user_choise = input("Введите: ")
            if user_choise not in ["1","2","3","4","5"]:
                print("Ошибка")
            else:
                break
    match user_choise:
            case '1':
                for key in data:
                    name1, name2, name3 = key.split()
                    if name1 == user_input:
                        print(f"{key} {data[key]}")
            case '2':
                for key in data:
                    name1, name2, name3 = key.split()
                    if name2 == user_input:
                        print(f"{key} {data[key]}")
            case '3':
                for key in data:
                    name1, name2, name3 = key.split()
                    if name3 == user_input:
                        print(f"{key} {data[key]}")
            case '4':
                for key, value in data.items():
                    if value == user_input:
                        print(f"{key} {data[key]}")
            case '5':
                print('Выход')
                return

# if __name__ == "__main__": - Когда интерпретатор Python читает 
# исходный файл, он исполняет весь найденный в нем код.
if __name__ == "__main__": 
    main()
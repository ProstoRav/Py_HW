def show(book):
    with open(book, 'r', encoding='utf-8') as file:
        print(file.read())
    print()

def create(book):
    with open(book, 'a', encoding='utf-8') as file: 
        i = input('Введите имя: ')
        f = input('Введите фамилию: ') 
        o = input('Введите отчество: ') 
        n = input('Введите номер телефона: ')
        file.write('\n')
        file.write(f'{i},{f},{o},{n}')
        print(f'Добавлена запись: {i},{f},{o},{n}')

def search(book):
    with open(book, 'r', encoding='utf-8') as file:
        our_book = file.read().split('\n')
        temp = input('Введите слово для поискового запроса: ')
        for i in our_book:
            if temp in i:
                print(i)

def edit(book):
    with open(book, 'r', encoding='utf-8') as file:
        our_book = file.read()
        print()
        print(our_book)
        print()
    index = int(input('Введите номер строки для редактирования: ')) - 1
    lines = our_book.split('\n')
    line = lines[index]
    elements = line.split(',')
    i = input('Введите имя: ')
    f = input('Введите фамилию: ') 
    o = input('Введите отчество: ') 
    n = input('Введите номер телефона: ')
    if len(i) == 0:
        i = elements[0]
    if len(f) == 0:
        f = elements[1]
    if len(o) == 0:
        o = elements[2]
    if len(n) == 0:
        n = elements[3]
    edited = f'{i},{f},{o},{n}'
    lines[index] = edited
    print(f'Запись "{line}" изменена на "{edited}"\n')
    with open(book, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

def delete(book):
    with open(book, 'r', encoding='utf-8') as file:
        our_book = file.read()
        print()
        print(our_book)
        print()
    index = int(input('Введите номер строки для удаления: ')) - 1
    lines = our_book.split('\n')
    line = lines[index]
    lines.pop(index)
    print(f'Удалена запись: "{line}"\n')
    with open(book, 'w', encoding='utf-8') as file:
        file.write('\n'.join(lines))
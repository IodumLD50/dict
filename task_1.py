
pets = dict()
#data = dict()
while True:
    name = input("Введите имя питомца (или Enter - для просмотра информации): ")
    if not name:
        name = input('Введите имя питомца на котого нужна информация (или Enter - для просмотра базы данных): ')
        if not name:
            print(pets)
            break
        try:
            print(pets[name])
        except:
            print('Такой питомец ещё не записан!')
            print(pets)
        break
    typ = input('Введите вид питомца: ')
    age = int(input('Введите возраст: '))
    owner = input('Введите имя владельца: ')
    t = 'Вид питомца'
    a = 'Возраст питомца'
    o = 'Имя владельца'
    data = {t: typ, a: age, o: owner}
    pets[name] =  data


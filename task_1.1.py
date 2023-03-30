
pets = dict()

while True:
    name = input("Введите имя питомца (или Enter - для просмотра информации): ")
    if not name:
        print(pets)
        break
       
    typ = input('Введите вид питомца: ')
    age = int(input('Введите возраст: '))
    owner = input('Введите имя владельца: ')
    t,a,o = 'Вид питомца','Возраст питомца','Имя владельца'
    data = {t: typ, a: age, o: owner}
    pets[name] =  data



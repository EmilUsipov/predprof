f = open('game.txt','r', encoding='UTF-8').readlines()

data_names = dict()
for data in f[1:]:
    GameName, characters, nameError, date = data.split('$')
    if characters in data_names:
        data_names[characters] += [GameName]
    else:
        data_names[characters] = [GameName]
question = input('Введите имя персонажа: ')
while question != 'game':
    if question in data_names.keys():
        c = 0
        print('Персонаж <characters> встречается в играх: \n')
        for games in data_names[question]:
            c += 1
            if c > 5: break
            print(f'{games}\n')
    else:
        print('Этого персонажа не существует')
    question = input('Введите имя персонажа или "game" для остановки: ')
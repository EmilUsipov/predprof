import csv

def obj_counter(data, target):
    '''
    :param data: list - БД, в которой осуществляется поиск
    :param target: string - Объект, количество упоминаний которого ищем
    :return: int - количество упоминаний в БД
    '''
    return data.count(target)

with open('game_counter.csv','w',encoding='UTF-8') as file:
    w = csv.writer(file, delimiter=',')
    w.writerow(['GameName','characters','nameError','date','counter'])

f = open('game.txt','r', encoding='UTF-8').readlines()

game_list = []
for data in f[1:]:
    GameName, characters, nameError, date = data.split('$')
    game_list.append(GameName)

for data in f[1:]:
    GameName, characters, nameError, date = data.split('$')
    counter = obj_counter(game_list, GameName)
    with open('game_counter.csv', 'a', encoding='UTF-8') as file:
        w = csv.writer(file, delimiter=',')
        w.writerow([GameName, characters, nameError, date, counter])
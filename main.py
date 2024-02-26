import csv

with open('game_new.csv','w',encoding='UTF-8') as file:
    w = csv.writer(file, delimiter=',')
    w.writerow(['GameName','characters','nameError','date'])

f = open('game.txt','r', encoding='UTF-8').readlines()

for data in f[1:]:
    GameName, characters, nameError, date = data.split('$')

    if '55' in nameError:
        nameError = 'DONE'
        date = '0000-00-00'

    with open('game_new.csv','a',encoding='UTF-8') as file:
        w = csv.writer(file,delimiter=',')
        w.writerow([GameName,characters,nameError,date])
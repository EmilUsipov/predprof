import csv

def gen_hash(name):
    alph = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-'
    d = {l: i for i, l in enumerate(alph,1)}
    p = 65
    m = 10**9+9
    hash_value = 0
    p_pow = 1
    for c in name:
        hash_value = (hash_value + d[c] * p_pow) % m
        p_pow = (p_pow * p) % m
    return int(hash_value)


with open('game_with_hash.csv','w',encoding='UTF-8') as file:
    w = csv.writer(file, delimiter=',')
    w.writerow(['GameName','characters','nameError','date','hash'])

f = open('game.txt','r', encoding='UTF-8').readlines()


for data in f[1:]:
    GameName, characters, nameError, date = data.split('$')

    hash_name = (GameName.replace(' ','')+characters).replace(':','').replace("'",'').replace('.','')
    hash = gen_hash(hash_name)

    with open('game_with_hash.csv', 'a', encoding='UTF-8') as file:
        w = csv.writer(file, delimiter=',')
        w.writerow([GameName, characters, nameError, date, hash])
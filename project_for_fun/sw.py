from sys import exit
from textwrap import dedent
import random
import Battle_scene
import Phrases
import Dicts


""" Объявляю класс бойцов на арене """


class Warrior(object):
    def __init__(self, hp, name):
        self.hp = hp
        self.name = name


Amir = Warrior(100, 'Amir')
Razak = Warrior(100, 'Razak')
Edmund = Warrior(100, 'Edmund')
Dragon = Warrior(300, 'Dragon')


""" Объвляю класс снаряжения """
class Equip():
    def __init__(self, name, count, dmg, armor):
        self.name = name
        self.count = count
        self.dmg = dmg
        self.armor = armor


sword = Equip(Dicts.items['sword'], 0, 10, 0)
shield = Equip(Dicts.items['shield'], 0, 0, 10)


class Other_Equip():
    def __init__(self, name, count):
        self.name = name
        self.count = count


food = Other_Equip(Dicts.other_equip['food'], 0)
gold = Other_Equip(Dicts.other_equip['gold'], 1000)
lvl = Other_Equip(Dicts.other_equip['lvl'], 0)
HP_status = Other_Equip(Dicts.other_equip['HP_status'], 100)
# new_hp = Equip(Dicts.other_equip['new_hp'], None)



'''Начало игры, небольшое вступление, нужно Выйти на улицу'''


def start():
    hello(dedent(Phrases.phrase_used_in_the_beginning_game))
    print('1 - Выйти из дома\n2 - Осмотреть дом?')
    choice = input('> ')
    if choice == '1':
        hello(dedent(Phrases.phrase_used_after_leaving_the_house)) # Выход из дома
        return street()
    elif choice == '2':
        print(dedent(Phrases.phrase_used_if_player_choose_to_stay_at_home)) # Осмотреться вокруг
        street()
    else:
        print(dedent(Phrases.phrase_used_if_player_choose_to_stay_at_home_Leaving_out)) # Принудительно покидаем дом
        return street()

'''Объявляю локацию улица (Fork). Развилка на 3 дороги Арена, Рынок и Дворец'''
def street():
    print(Phrases.phrase_used_at_the_fork) # На развилке
    print(f'1 - {Dicts.places["arena"]}\n2 - {Dicts.places["market"]}\n3 - {Dicts.places["palace"]}')
    choice = input('> ')
    if choice == '1':
        hello(f'''....................................
        Вы пришли {Dicts.places["arena"]}, чем займетесь?''')
        return arena()
    elif choice == '2':
        hello(f'''....................................
        Вы пришли {Dicts.places["market"]}''')
        return main_market()
    elif choice == '3':
        hello(f'''....................................
        Вы пришли {Dicts.places["palace"]}, чем займетесь?''')
        return palace()
    else:
        print('Нужно выбрать из списка.')
        return street()


'''объявляю локацию арена с выбором бойцов'''
def arena():
    print(f'Здоровье {HP_status.count}')
    print(f'Мечь {sword.count}')
    print(f'Щит {shield.count}')
    print(f'Еда {food.count}')
    print(f'Уровень {lvl.count}')
    print(f'Золото {gold.count}')
    print(f'Amir = {Amir.hp}')

    print('1 - поковыряться в носу\n2 - ознакомиться со списком противников\n3 - вернуться к развилке.')
    choice = input('> ')
    if choice == '1':
        print('Кажется, вы сломали себе палец, попробуйте начать заново или восполните здоровье')
        print('1 - Начать заново\n2 - Съесть шаурму')
        choice = input('> ')
        if choice == '1':
            start()
        elif choice == '2' and food.count > 0:
            shava()
        elif choice == '2' and food.count == 0:
            print('У вас нету шаурмы, но она продается на рынке.')
            print('Попробуйте еще раз')
            return  arena()
        else:
            print('Нужно выбрать из списка.')
            return arena()
    elif choice == '3':
        return street()
    elif choice == '2':
        print('У вас 3 противника на выбор: 1 - Amir, 2 - Razak, 3 - Edmund')
        choice = input('>')
        if choice == '1':
            return battle_with_enemy_in_arena(Amir)
        elif choice == '2':
            return battle_with_enemy_in_arena(Razak)
        elif choice == '3':
            return battle_with_enemy_in_arena(Edmund)
        else:
            print('Нужно выбрать из списка.')
            return arena()
    else:
        print('Нужно выбрать из списка')
        arena()


def battle_with_enemy_in_arena(warrior):
    print(f'Вы вызвали на бой {warrior.name}')
    Battle_scene.battle(warrior.name, HP_status.count, warrior.hp, sword.count, shield.count)
    lvl.count += 1
    return arena()


'''Объявляю локацию Дворец. Там будет либо король, либо дракон.
Нужно связать с победами на арене'''
def palace():
    print('1 - Пойти дальше\n2 - вернуться')
    choice = input('> ')
    if choice == '1' and lvl.count >= 3:
        print('Вы попали в покои короля!')
        king_palace()
    elif choice == '1' and lvl.count < 3:
        print(f'Твой уровень: {lvl.count}. Ты еще очень слаб. Чтобы пройти дальше ты должен достигнуть 3го уровня.')
        print('Тебя вышвыривают из дворца пинком под зад.')
        street()
    elif choice == '2':
        street()
    else:
        print('нужно выбирать из предлженного списка')
        palace()

def king_palace():
    chance = random.randint(1, 2)
    if chance == 1:
        print('Король')
    else:
        print('На вас напал Дракон из подземелья')
        Battle_scene.battle('Дракон', HP_status.count, Dragon.hp)



'''Объявляю локацию рынок выбор Купить или Украсть'''
def main_market():
    print('Вы подошли к купцу и видите на прилавке: ')
    print(f'1 - {Dicts.items["sword"]}\n2 - {Dicts.items["shield"]}\n3 - {Dicts.other_equip["food"]}'
                                                    '\n4 - вернуться на улицу\nчто выберите?')
    choice = input()
    if choice == '1':
        buing_item_at_market(sword)
    elif choice == '2':
        buing_item_at_market(shield)
    elif choice == '3':
        buing_item_at_market(food)
    elif choice == '4':
        return street()
    else:
        print('Нужно выбрать из списка')
        return main_market()


'''Торговля на рынке Украсть или купить'''
def buing_item_at_market(item):
    print(dedent('''                            ***
                            \t\t\t\t\tКупить или украсть?
                            \t\t\t\t\t1 - купить
                            \t\t\t\t\t2 - украсть'''))
    choice = input('> ')
    if choice == '1':
        if item.count >= 1:
            print(f'У вас уже есть {item.name}, Вы больше не унесете')
            return main_market()
        else:
            print('....................................')
            print(f'Поздравляю! Вы купили {item.name}.')
            item.count += 1
            gold.count -= 300
            return main_market()
    elif choice == '2':
        return theft_of_an_item(item)
    else:
        print('Выбери действие')
        return buing_item_at_market()


'''Поведение продавца при краже рандом'''
def theft_of_an_item(item):
    seller = random.randint(1, 2)
    if seller == 1:
        print('....................................')
        dead('Не повезло! Продавец заметил вашу кражу и позвал охрану')
    else:
        if item.count >= 1:
            print(f'У вас уже есть {item.name}, Вы больше не унесете')
            return main_market()
        else:
            print('....................................')
            print(f'Поздравляю! Кража прошла успешно. Теперь у вас есть {item.name}, и деньги на еще что-нибудь')
            item.count += 1
            input('Продолжить> ')
            return main_market()


'''Отравимся или нет при поедании шаурмы рандом'''
def shava():
    print('Какая вкусная шаурма')
    shavuha = random.randint(1, 2)
    if shavuha == 1:
        print('Вы полны сил и готовы идти дальше')
        input('Продолжить>')
        food.count -= 1
        return arena()
    else:
        dead('Вы отравились Шаурмой, очень печально')


'''функция на выход из игры при проигрыше'''
def dead(why):
    print(why, '\nВы проиграли.')
    exit(0)


'''функция приветствия. Вставляется перед каждой локацией'''
def hello(word):
    print(word)





start()

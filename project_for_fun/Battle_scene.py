from random import randint


def battle(name, my_hp, enemy_hp, sword, shield):

    while my_hp > 0 and enemy_hp > 0:
        attack = randint(1, 2)

        if attack == 1:
            if sword == 1:
                print(f'Вы наносите удар. {name} получает урон в 20 очков здоровья!')
                enemy_hp -= 20
                print(f'здоровье противника: {enemy_hp}')
                input('продолжить>')
            else:
                print(f'Вы наносите удар. {name} получает урон в 10 очков здоровья!')
                enemy_hp -= 10
                print(f'здоровье противника: {enemy_hp}')
                input('продолжить>')

        else:
            if shield == 1:
                print(f'{name} наносит удар. Вы теряете 20 очков здоровья')
                my_hp -= 20
                print(f'Ваше здоровье:{my_hp}')
                input('продолжить>')
            else:
                print(f'{name} наносит удар. Вы теряете 25 очков здоровья')
                my_hp -= 25
                print(f'Ваше здоровье:{my_hp}')
                input('продолжить>')
    if my_hp == 0:
        print('Вы проиграли, попробуйте еще раз.')
    else:
        print('Поздравляю! Вы победили. Так же вы повысили свой уровень на 1')

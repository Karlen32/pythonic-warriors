from random import randint


class Character:
    # Базовые атрибуты
    BRIEF_DESC_CHAR_CLASS = 'отважный искатель приключений'
    RANGE_VALUE_ATTACK = (1, 3)
    RANGE_VALUE_DEFENCE = (1, 5)
    SPECIAL_BUFF = 15
    SPECIAL_SKILL = 'Удача'

    def __init__(self, name: str):
        self.name = name

    def attack(self) -> str:
        value_attack = 5 + randint(*self.RANGE_VALUE_ATTACK)
        return f'{self.name} нанёс урон противнику равный {value_attack}.'

    def defence(self) -> str:
        value_defence = 10 + randint(*self.RANGE_VALUE_DEFENCE)
        return f'{self.name} блокировал {value_defence} урона.'

    def special(self) -> str:
        return (f'{self.name} применил специальное умение '
                f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}".')

    def __str__(self) -> str:
        return f'{self.__class__.__name__} — {self.BRIEF_DESC_CHAR_CLASS}.'


class Warrior(Character):
    BRIEF_DESC_CHAR_CLASS = 'дерзкий воин ближнего боя'
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    SPECIAL_BUFF = 25
    SPECIAL_SKILL = 'Выносливость'


class Mage(Character):
    BRIEF_DESC_CHAR_CLASS = 'находчивый воин дальнего боя'
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (-2, 2)
    SPECIAL_BUFF = 40
    SPECIAL_SKILL = 'Атака'


class Healer(Character):
    BRIEF_DESC_CHAR_CLASS = 'могущественный заклинатель'
    RANGE_VALUE_ATTACK = (-3, -1)
    RANGE_VALUE_DEFENCE = (2, 5)
    SPECIAL_BUFF = 30
    SPECIAL_SKILL = 'Защита'


def choice_char_class(char_name: str) -> Character:
    """Выбор класса персонажа."""
    game_classes = {'warrior': Warrior, 'mage': Mage, 'healer': Healer}
    approve_choice = None

    while approve_choice != 'y':
        selected_class = input(
            'Введи название персонажа: Воитель — warrior, '
            'Маг — mage, Лекарь — healer: '
        )
        char_class = game_classes[selected_class](char_name)
        print(char_class)
        approve_choice = input(
            'Нажми (Y), чтобы подтвердить выбор, '
            'или любую другую кнопку, чтобы выбрать другого персонажа '
        ).lower()
    return char_class


def start_training(character: Character) -> str:
    """Тренировка персонажа."""
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — для атаки, defence — для защиты, '
          'special — для использования суперсилы.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(character.attack())
        if cmd == 'defence':
            print(character.defence())
        if cmd == 'special':
            print(character.special())
    return 'Тренировка окончена.'


def main():
    """Основная функция запуска игры."""
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    character = choice_char_class(char_name)
    print(start_training(character))


if __name__ == '__main__':
    main()


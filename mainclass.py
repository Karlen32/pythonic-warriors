from random import randint

DEFAULT_ATTACK = 5
DEFAULT_DEFENCE = 10
DEFAULT_STAMINA = 80


class Character:

    BRIEF_DESC_CHAR_CLASS = 'отважный искатель приключений'
    RANGE_VALUE_ATTACK = (1, 3)
    RANGE_VALUE_DEFENCE = (1, 5)
    SPECIAL_SKILL = 'Удача'
    SPECIAL_BUFF = 15
    STAMINA = DEFAULT_STAMINA

    def __init__(self, name: str):
        self.name = name

    def attack(self) -> str:
        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return f'{self.name} нанёс противнику урон равный {value_attack}.'

    def defence(self) -> str:
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return f'{self.name} блокировал {value_defence} урона.'

    def special(self) -> str:
        return (f'{self.name} применил специальное умение '
                f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}", '
                f'выносливость увеличена на {self.STAMINA}.')

    def __str__(self) -> str:
        return f'{self.__class__.__name__} — {self.BRIEF_DESC_CHAR_CLASS}.'


class Warrior(Character):
    BRIEF_DESC_CHAR_CLASS = 'дерзкий воин ближнего боя. Сильный, выносливый и отважный'
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    SPECIAL_SKILL = 'Выносливость'
    SPECIAL_BUFF = DEFAULT_STAMINA + 25


class Mage(Character):
    BRIEF_DESC_CHAR_CLASS = 'находчивый воин дальнего боя. Обладает высоким интеллектом'
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (-2, 2)
    SPECIAL_SKILL = 'Атака'
    SPECIAL_BUFF = DEFAULT_ATTACK + 40


class Healer(Character):
    BRIEF_DESC_CHAR_CLASS = 'могущественный заклинатель. Черпает силы из природы, веры и духов'
    RANGE_VALUE_ATTACK = (-3, -1)
    RANGE_VALUE_DEFENCE = (2, 5)
    SPECIAL_SKILL = 'Защита'
    SPECIAL_BUFF = DEFAULT_DEFENCE + 30


def choice_char_class(char_name: str) -> Character:
  
    game_classes = {'warrior': Warrior, 'mage': Mage, 'healer': Healer}
    approve_choice: str = None

    while approve_choice != 'y':
        selected_class = input(
            'Введи название персонажа, за которого хочешь играть: '
            'Воитель — warrior, Маг — mage, Лекарь — healer: '
        ).lower()

        if selected_class not in game_classes:
            print('Такого персонажа нет. Попробуй ещё раз.')
            continue

        char_class: Character = game_classes[selected_class](char_name)
        print(char_class)

        approve_choice = input(
            'Нажми (Y), чтобы подтвердить выбор, '
            'или любую другую кнопку, чтобы выбрать другого персонажа: '
        ).lower()

    return char_class


def start_training(character: Character) -> str:

    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — атаковать, '
          'defence — блокировать, special — использовать суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')

    commands = {
        'attack': character.attack,
        'defence': character.defence,
        'special': character.special
    }

    cmd = None
    while cmd != 'skip':
        cmd = input('Введи команду: ').lower()
        if cmd in commands: 
            print(commands[cmd]())
      

    return 'Тренировка окончена.'
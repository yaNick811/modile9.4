import random

first = 'Мама мыла раму'
second = 'Рамена мало было'
result = list(map(lambda x, y: x == y, first, second))
print(result)

# Замыкание
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for item in data_set:
                file.write(str(item) + '\n')
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# Класс MysticBall
class MysticBall:
    def __init__(self, words):
        self.words = words

    def __call__(self):
        return random.choice(self.words)

# Пример использования класса MysticBall
words_collection = ['слово1', 'слово2', 'слово3', 'слово4']
mystic_ball = MysticBall(words_collection)
print(mystic_ball())
print(mystic_ball())
print(mystic_ball())
print(mystic_ball())
print(mystic_ball())


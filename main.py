words_easy = {'said': 'говорить', 'each': 'каждый', 'does': 'делает', 'also': 'также', 'end': 'конец' }
words_medium = {' cut': 'резать', ' large': 'большой', 'spell': 'читать по буквам', 'land': 'земля', 'follow': 'следовать'}
words_hard = {'change': 'менять', 'kind': 'добрый', 'animal': 'животное', 'earth': 'земля', 'after': 'после'}

answers = {}
levels = {
    0: 'Нулевой',
    1: 'Так себе',
    2: 'Можно лучше',
    3: 'Норм',
    4: 'хорошо',
    5: 'Отлично',
}
print(f"Выберите уровень сложности: \n легкий\n средний\n сложный")
user_input = input('Введите уровень сложности: ').lower()
if user_input == 'сложный':
    words = words_hard
if user_input == 'средний':
    words = words_medium
else:
    words = words_easy

words_count = len(words)

print(f"Выбран уровень сложности, мы предложим {words_count} слов, подберите перевод ")

for word_en, word_ru in words.items():

    print("Нажмите Enter")
    input()

    letter_count = len(word_ru)
    first_letter = word_ru[0]

    print(f"{word_en}, {letter_count} букв, начинается на {first_letter}...")

    user_input = input().lower()
    if user_input == word_ru:
        print(f"Верно, {word_en.title()} это {word_ru}")
        answers[word_en] = True
    else:
        print(f"Неверно, {word_en.title()} это {word_ru}")
        answers[word_ru]=False

correct_words = []
incorrect_words = []


for word_en, is_correct in answers.items():
    if is_correct:
        correct_words.append(word_en)
    else:
        incorrect_words.append(word_en)

print(f"Првавильно отвеченные слова: ")
print("\n".join(correct_words))
print(f"Непрвавильно отвеченные слова: ")
print("\n".join(incorrect_words))

"""Выводим уровень пользователя"""

correct_count = len(correct_words)
user_level = levels[correct_count]

print()
print(f"Ваш ранг: \n {user_level}")
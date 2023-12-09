import random

words = ['code', 'bit', 'list', 'soul', 'next']
answers = []
MORSE_CODES = {
  "0": "-----",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--..",
  ".": ".-.-.-",
  ",": "--..--",
  "?": "..--..",
  "!": "-.-.--",
  "-": "-....-",
  "/": "-..-.",
  "@": ".--.-.",
  "(": "-.--.",
  ")": "-.--.-"
}


def morse_encode(world):
    """
    Функция переводит слова на английском языке в последовательности точек и тире.
    :param world: исходное слово
    :return: возвращает строку морзянки
    """
    word_encoded = []
    for letter in world:
        word_encoded.append(MORSE_CODES.get(letter, ""))
    return "".join(word_encoded)


print(morse_encode('divine'))



def get_word():
    """
    Получает случайное слово из списка.
    :return: строка слово
    """
    return random.choice(words)


def print_statistics(answers):
    """
    Вывод статистики на основе списка answers типа [True, False, False, True, False]
    :param answers:
    :return Список верности ответов
    """

    answers_total = len(answers)
    answers_correct = sum(answers)
    answers_incorrect = answers_total - answers_correct

    print(f"""
    Всего задачек: {answers_total}
    Отвечено верно: {answers_correct}
    Отвечено неверно: {answers_incorrect}
    """)


def main():
    print(f"Сегодня мы потренеруемся расшифрововать азбуку Морзе")
    print("Нажмите Enter и начнем")
    input()
    for i in range(1, len(words)+1):
        current_word = get_word()
        current_encoded = morse_encode(current_word)
        print(f"Слово {i} {current_encoded}")
        user_input = input()

        if user_input.lower() == current_word:
            print(f"Верно {current_word}!")
            answers.append(True)
        else:
            print(f"Неверно {current_word}!")
            answers.append(False)

        print_statistics(answers)

main()

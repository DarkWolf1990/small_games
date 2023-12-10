import random
from config import WORDS_PATH, HISTORY_PATH

def get_word_from_file():
    """
    Получаем все слова из файла спискам
    :return:
    """

    with open(WORDS_PATH, 'r', encoding='utf-8' ) as file:
        lines = file.read()
        words =lines.splitlines()

        return words


def shuffle_word(word):
    """
    Перемешивает буквы в слове
    :param word:
    :return: возвращает перемешанное слово
    """
    word_as_list = list(word)
    random.shuffle(word_as_list)
    return ''.join(word_as_list)


def save_player_score(player_name, player_score):
      with open(HISTORY_PATH, 'a', encoding='utf-8') as fp:
        fp.write(f"{player_name} {player_score}\n")


def get_statistics_from_file():
    scores = []
    with open(HISTORY_PATH, 'r', encoding='utf-8') as fp:
        for line in fp:
            score= line.strip().split(" ")[-1]
            scores.append(score)
    max_score = max(scores)
    games_played = len(scores) - 1
    return {"max_score": max_score, "games_played": games_played}


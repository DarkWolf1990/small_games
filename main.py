from utils import get_word_from_file, shuffle_word, save_player_score, get_statistics_from_file


def main():
    user_score = 0
    point_ = 10
    print("Введите ваше имя: ")
    user_name_ = input()
    words = get_word_from_file()
    for word in words:
        word_shuffled = shuffle_word(word)
        print(f"Угадайте слово: {word_shuffled}")

        user_input = input()

        if user_input == word:
            user_score += point_
            print(f"Верно! Вы получаете 10 очков.")
        else:
            print(f"Неверно! Верный ответ - {word}")

    save_player_score(user_name_, user_score )
    stats = get_statistics_from_file()


    print(f"Всего игр сыграно: {stats.get('games_played')}")
    print(f"Максимальный рекорд {stats.get('max_score')}")


main()
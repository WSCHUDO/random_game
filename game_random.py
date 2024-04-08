import random

def guess_the_word_game():
    level_words = {
        1: ["кошка", "собака", "лошадь", "корова", "свинья"],
        2: ["яблоко", "банан", "вишня", "груша", "дыня"],
        3: ["москва", "париж", "лондон", "берлин", "рим"]
    }

    def play_level(level, words):
        word = random.choice(words)
        hint = word[0]
        attempt = 0
        print(f"Уровень {level}. Я загадал слово, попробуйте угадать его.")
        while True:
            attempt += 1
            user_input = input("Ваша попытка: ").lower().strip()
            if user_input == 'подсказка':
                if attempt % 2 == 0:
                    print(f"Подсказка: буква '{hint}'")
                else:
                    print("Подсказка будет доступна на следующей попытке.")
            elif user_input == word:
                print(f"Вы угадали! Вы проходите на следующий уровень.")
                break
            else:
                print("Неверно, попробуйте ещё раз.")

    for level in range(1, 4):
        play_level(level, level_words[level])

    print("Поздравляю! Вы выиграли и прошли все уровни. Хотите начать игру заново? (да/нет)")
    if input().lower().strip() == 'да':
        guess_the_word_game()
    else:
        print("Спасибо за игру! До свидания!")

# Запуск игры
guess_the_word_game()

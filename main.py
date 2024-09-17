import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# Создаём функцию, которая будет получать информацию
def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        # Создаём объект Soup
        soup = BeautifulSoup(response.content, "html.parser")
        # Получаем слово. text.strip удаляет все пробелы из результата
        english_word = soup.find("div", id="random_word").text.strip()
        # Получаем описание слова
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        return {
            "english_word": english_word,
            "word_definition": word_definition
        }
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Создаём функцию, которая будет делать саму игру
def word_game():
    translator = Translator()
    print("Добро пожаловать в игру!")
    while True:
        # Создаём функцию, чтобы использовать результат функции-словаря
        word_dict = get_english_words()
        english_word = word_dict.get("english_word")
        word_definition = word_dict.get("word_definition")

        # Переводим слово и определение на русский
        russian_word = translator.translate(english_word, dest='ru').text
        russian_definition = translator.translate(word_definition, dest='ru').text

        # Начинаем игру
        print(f"Значение слова - {russian_definition}")
        user = input("Что это за слово? ")
        if user == russian_word:
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {russian_word}")

        # Создаём возможность закончить игру
        play_again = input("Хотите сыграть еще раз? д/н ")
        if play_again != "y":
            print("Спасибо за игру!")
            break

word_game()


from urllib.request import urlopen
from random import randint


def word_list_sum(word_list):
    sum = 0
    for word, value in word_list.items():
        sum += value
    return sum


def retrieve_random_word(word_list):
    rand_index = randint(1, word_list_sum(word_list))
    for word, value in word_list.items():
        rand_index -= value
        if rand_index <= 0:
            return word


def build_word_dict(text):
    # Удаляем символы новой строки и кавычки
    text = text.replace("\n", " ")
    text = text.replace("\"", "")

    # Убедитесь, что знаки препинания обрабатываются как самостоятельные "слова"
    # таким образом они будут включены в марковскую цепь
    punctuation = [',', '.', ';', ':']
    for symbol in punctuation:
        text = text.replace(symbol, " " + symbol + " ")

    words = text.split(" ")
    # Удалите пустые слова
    words = [word for word in words if word != ""]

    word_dict = {}
    for i in range(1, len(words)):
        if words[i - 1] not in word_dict:
            # Создаем новый словарь для этого слова
            word_dict[words[i - 1]] = {}

        if words[i] not in word_dict[words[i - 1]]:
            word_dict[words[i - 1]][words[i]] = 0

        word_dict[words[i - 1]][words[i]] += 1

    return word_dict


content = str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(), 'utf-8')
wordDict = build_word_dict(content)

# Генерируем цепь Маркова длиной 100
length = 100
chain = ""
currentWord = "I"
for i in range(0, length):
    chain += currentWord + " "
    currentWord = retrieve_random_word(wordDict[currentWord])

print(chain)

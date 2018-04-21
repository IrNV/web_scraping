from nltk import bigrams
from nltk.book import *
from nltk import FreqDist
from nltk import ngrams

# Поиск двуграмм
bigrams = bigrams(text6)
bigramsDist = FreqDist(bigrams)
# Проверяем сколько раз встречается двуграмма Sir Robin
print(bigramsDist[("Sir", "Robin")])

# Поиск 4-грамм
fourgrams = ngrams(text6, 4)
fourgramsDist = FreqDist(fourgrams)
# Проверяем сколько раз встречается 4-грамма farhter smelt of elderberries
print(fourgramsDist[("father", "smelt", "of", "elderberries")])

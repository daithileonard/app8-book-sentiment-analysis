import nltk
import re

from nltk.corpus import stopwords
english_stopwords = stopwords.words("english")

with open("miracle_in_the_andes.txt", "r", encoding="utf8") as file:
    book = file.read()

pattern = re.compile("[a-zA-Z]+")
findings = re.findall(pattern, book.lower())

d = {}
for word in findings:
    if word in d.keys():
        d[word] = d[word]+1
    else:
        d[word]=1

d_list = [(value, key) for (key, value) in d.items()]
sorted(d_list, reverse=True)

filtered_words = []
for count, word in d_list:
    if word not in english_stopwords:
        filtered_words.append((count, word))


# print(english_stopwords)
# print(d_list)
print(sorted(filtered_words, reverse=True))


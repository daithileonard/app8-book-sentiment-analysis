import nltk
import re
from nltk.sentiment import SentimentIntensityAnalyzer

with open("miracle_in_the_andes.txt", "r", encoding="utf8") as file:
    book = file.read()

analyzer = SentimentIntensityAnalyzer()
# result = analyzer.polarity_scores(book)

pattern = re.compile("Chapter [0-9]+")
chapters = re.split(pattern, book)
chapters = chapters[1:]

for chapter in chapters:
    scores = analyzer.polarity_scores(chapter)
    print(scores)

# print(result)
# print(chapters)


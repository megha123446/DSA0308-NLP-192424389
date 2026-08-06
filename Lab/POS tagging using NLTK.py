import nltk
from nltk.tokenize import word_tokenize

nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")

text = "The boys are running and the girls are playing in the park."

words = word_tokenize(text)
tags = nltk.pos_tag(words)

for word, tag in tags:
    print(word, tag)

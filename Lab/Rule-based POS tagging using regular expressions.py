import nltk

patterns = [
    (r".*ing$", "VBG"),
    (r".*ed$", "VBD"),
    (r".*es$", "VBZ"),
    (r".*ly$", "RB"),
    (r".*ous$", "JJ"),
    (r".*s$", "NNS"),
    (r".*", "NN")
]

tagger = nltk.RegexpTagger(patterns)

words = ["running", "walked", "quickly", "dangerous", "cars"]

for word, tag in tagger.tag(words):
    print(word, tag)

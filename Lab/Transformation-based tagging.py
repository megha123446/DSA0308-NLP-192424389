sentence = ["The", "boys", "play", "games"]

tags = []

for word in sentence:
    if word[0].isupper():
        tags.append("NNP")
    else:
        tags.append("NN")

for i in range(len(sentence)):
    if sentence[i].endswith("s"):
        tags[i] = "NNS"

    if sentence[i].endswith("y"):
        tags[i] = "JJ"

for word, tag in zip(sentence, tags):
    print(word, tag)

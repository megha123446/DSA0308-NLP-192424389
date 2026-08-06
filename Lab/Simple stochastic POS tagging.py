from collections import defaultdict

training_data = [
    [("The", "DT"), ("cat", "NN"), ("runs", "VB")],
    [("A", "DT"), ("dog", "NN"), ("barks", "VB")],
    [("The", "DT"), ("dog", "NN"), ("runs", "VB")]
]

word_tag_count = defaultdict(lambda: defaultdict(int))
tag_count = defaultdict(int)

for sentence in training_data:
    for word, tag in sentence:
        word_tag_count[word.lower()][tag] += 1
        tag_count[tag] += 1

sentence = "The cat barks"

for word in sentence.split():
    word = word.lower()

    if word in word_tag_count:
        tag = max(word_tag_count[word], key=word_tag_count[word].get)
    else:
        tag = max(tag_count, key=tag_count.get)

    print(word, tag)

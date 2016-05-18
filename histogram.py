import string
import operator

with open("sample.txt") as opened_file:
    text = opened_file.read().lower()

for i in string.punctuation:
    text = text.replace(i, "")
    text = text.replace("\n", " ")
    text = text.replace("  ", " ")

histogram = {}

for word in text.split(" "):
    if word in histogram.keys():
        histogram[word] += 1
    else:
        histogram[word] = 1

sorted_hist = sorted(histogram.items(), key=operator.itemgetter(1))
for idx, item in enumerate(sorted_hist[:-21:-1]):
    word, count = item
    print(idx + 1, word, count)
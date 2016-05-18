import string

with open("sample.txt") as opened_file:
    text = opened_file.read().lower()

for i in string.punctuation:
    text = text.replace(i, "")

histogram = {}

for word in text.split(" "):
    if word in histogram.keys():
        histogram[word] += 1
    else:
        histogram[word] = 1

for key, value in histogram.items():
    print(key, value)
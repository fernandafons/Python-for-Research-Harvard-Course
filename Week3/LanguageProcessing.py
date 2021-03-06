import os
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt


def count_words(text):
    """
    Count the numer of times each word occurs in text. Return dictionary where keys are
     unique words and values are word counts. Skip punctuation.
    """

    text = text.lower()
    skips = [".", ",", ";", ":", "'", '"']
    for ch in skips:
        text = text.replace(ch, "")
    word_counts = {}
    for word in text.split(" "):
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    # print(word_counts)
    return word_counts


text = "This is. my text"
from collections import Counter

def count_words_fast(text):
    """
    Count the number of times each word occurs in text. Return dictionary where keys are
     unique words and values are word counts. Skip punctuation.
    """

    text = text.lower()
    skips = [".", ",", ";", ":", "'", '"']
    for ch in skips:
        text = text.replace(ch, "")

    word_counts = Counter(text.split(" "))
    # print(word_counts)
    return word_counts


def read_book(title_path):
    """
    Read a book and return it as a string.
    """
    with open(title_path, "r", encoding="utf-8") as current_file:
        text = current_file.read()
        text.replace("\n", "").replace("\r", "")
    return text


text = read_book("Books/Books/English/shakespeare/Romeo and Juliet.txt")
word_counts = count_words(text)
german_text = read_book("Books/Books/German/shakespeare/Romeo und Julia.txt")
word_counts_ger = count_words(german_text)


def word_stats(word_counts):
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)

(num_unique, counts) = word_stats(word_counts)
# print(num_unique)
# print(sum(counts))
# print(counts)
(num_unique, counts) = word_stats(word_counts_ger)
# print(num_unique)


book_dir = "Books/Books"
print(os.listdir(book_dir))

stats = pd.DataFrame(columns = ("language", "author", "title", "length", "unique"))
title_num = 1

for language in os.listdir(book_dir):
    for author in os.listdir(book_dir + "/" + language):
        for title in os.listdir(book_dir + "/" + language + "/" + author):
            inputfile = book_dir + "/" + language + "/" + author + "/" + title
            # print(type(inputfile))
            text = read_book(inputfile)
            (num_unique, counts) = word_stats(count_words(text))
            stats.loc[title_num] = language, author.capitalize(), title.replace(".txt", ""), sum(counts), num_unique
            title_num += 1

print(stats.length)
print(stats[stats.language == "English"])
# print(stats.tail())


# plt.plot(stats.length, stats.unique, "bo")
# plt.show()

plt.figure(figsize=(10, 10))
subset = stats[stats.language == "English"]
plt.loglog(subset.length, subset.unique, "o", label = "English", color = "crimson")
subset = stats[stats.language == "French"]
plt.loglog(subset.length, subset.unique, "o", label = "French", color = "forestgreen")
subset = stats[stats.language == "German"]
plt.loglog(subset.length, subset.unique, "o", label = "German", color = "orange")
subset = stats[stats.language == "Portuguese"]
plt.loglog(subset.length, subset.unique, "o", label = "Portuguese", color = "blueviolet")
plt.legend()
plt.xlabel("Book length")
plt.ylabel("Number of unique words")
plt.savefig("lang_plot.pdf")
plt.show()
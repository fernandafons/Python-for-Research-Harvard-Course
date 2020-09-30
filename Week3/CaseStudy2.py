import pandas as pd
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
# from .LanguageProcessing import count_words_fast

# hamlets = pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@hamlets.csv",
#                       index_col=0)

# language, text = hamlets.iloc[0]
# print(language)
# print(text)

def read_book(title_path):
    """
    Read a book and return it as a string.
    """
    with open(title_path, "r", encoding="utf-8") as current_file:
        text = current_file.read()
        text.replace("\n", "").replace("\r", "")
    return text


text = read_book("Books/Books/English/shakespeare/Hamlet.txt")


def count_words_fast(text):
    """
    Count the number of times each word occurs in text. Return dictionary where keys are
     unique words and values are word counts. Skip punctuation.
    """
    text = str(text)
    text = text.lower()
    skips = [".", ",", ";", ":", "'", '"', "\n", "\\n"]
    for ch in skips:
        text = text.replace(ch, "")

    word_counts = Counter(text.split(" "))
    print(word_counts)

    return word_counts


count_words_fast(text)


def summarize_text(language, text):
    counted_text = count_words_fast(text)

    data = pd.DataFrame({
        "word": list(counted_text.keys()),
        "count": list(counted_text.values())
    })

    data.loc[data["count"] > 10, "frequency"] = "frequent"
    data.loc[data["count"] <= 10, "frequency"] = "infrequent"
    data.loc[data["count"] == 1, "frequency"] = "unique"

    data["length"] = data["word"].apply(len)

    sub_data = pd.DataFrame({
        "language": language,
        "frequency": ["frequent","infrequent","unique"],
        "mean_word_length": data.groupby(by = "frequency")["length"].mean(),
        "num_words": data.groupby(by = "frequency").size()
    })

    print(sub_data)
    return sub_data

summarize_text("Portuguese", text)
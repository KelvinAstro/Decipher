import tensorflow as tf


import matplotlib.pyplot as plt


import unicodedata
import re
import numpy as np
import os
import io
import time

path_to_file = "Newer01.txt"


def preprocess_sentence(w):
    w = "<start> " + w + " <end>"
    return w


def create_dataset(path, num_examples):
    lines = io.open(path, encoding="UTF-8").read().strip().split("\n")

    word_pairs = [
        [preprocess_sentence(w) for w in l.split(":")] for l in lines[:num_examples]
    ]

    # print(word_pairs)

    return zip(*word_pairs)


def tokenize(lang):
    lang_tokenizer = tf.keras.preprocessing.text.Tokenizer(filters="")
    lang_tokenizer.fit_on_texts(lang)

    tensor = lang_tokenizer.texts_to_sequences(lang)

    tensor = tf.keras.preprocessing.sequence.pad_sequences(tensor, padding="post")

    return tensor, lang_tokenizer


dataset = plaintxt, encryptxt = create_dataset(path_to_file, 10)

for i in range(len(plaintxt)):
    print(plaintxt[i])
    print(encryptxt[i])

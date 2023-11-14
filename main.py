# How a neural network language model works
import torch
import torch.nn as nn
import torch.optim as optim

raw_sentence = ["I like dog", "I love coffee", "I hate milk"]


def make_batch(sentences):
    input_batch = []
    target_batch = []

    for sen in sentences:
        word = sen.split()
        input = [word2id[n] for n in word[:-1]]
        target = word2id[word[-1]]

        input_batch.append(input)
        target_batch.append(target)

    return input_batch, target_batch


word_list = " ".join(raw_sentence).split()
word_list = list(set(word_list))
word2id = {w: i for i, w in enumerate(word_list)}
id2word = {i: w for i, w in enumerate(word_list)}
n_class = len(word2id)  # number of Vocabulary

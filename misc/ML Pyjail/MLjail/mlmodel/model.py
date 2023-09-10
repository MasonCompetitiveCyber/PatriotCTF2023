import os
import nltk
from nltk.stem.lancaster import LancasterStemmer
import numpy
import tensorflow as tf
import tflearn

import pickle

stemmer = LancasterStemmer()

ignore_char=["?", "!", ",", ".", "{", "}"]

words = []
labels = []
docs_x = []
docs_y = []


curr_path = os.getcwd()

tags_folder_path = os.path.join(curr_path, "tags")
tags_file_list = os.listdir(tags_folder_path)

for tag_file in tags_file_list:
    if tag_file[-3:] != 'txt':
        continue
    tag_name = tag_file[:-4]
    file_loc = os.path.join(tags_folder_path, tag_file)
    with open(file_loc, 'r') as f:
        for line in f.readlines():
            word = nltk.word_tokenize(line)
            words.extend(word)
            docs_x.append(word)
            docs_y.append(tag_name)
    if tag_name not in labels:
        labels.append(tag_name)

words = [stemmer.stem(w.lower()) for w in words if w not in ignore_char]
words = sorted(list(set(words)))
labels = sorted(labels)

training = []
output = []

out_empty = [0 for _ in range(len(labels))]

for x, doc in enumerate(docs_x):
    bag = []
    wrds = [stemmer.stem(w) for w in doc]
    for w in words:
        if w in wrds:
            bag.append(1)
        else:
            bag.append(0)
    output_row = out_empty[:]
    output_row[labels.index(docs_y[x])] = 1
    training.append(bag)
    output.append(output_row)

training = numpy.array(training)
output = numpy.array(output)

with open("training_data/data.pickle", "wb") as f:
    pickle.dump((words, labels, training, output), f)

tf.compat.v1.reset_default_graph()
net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)


model.fit(training, output, n_epoch=2000, batch_size=8, show_metric=False)
model.save("training_data/model.tflearn")

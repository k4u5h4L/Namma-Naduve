from django.conf import settings

from tensorflow.keras.models import load_model
import numpy as np
import pickle
import os
from tensorflow.keras.preprocessing.sequence import pad_sequences

model = load_model(
    f'{settings.BASE_DIR}/forum/neural_net/toxicity_model_dbms.h5')

with open(f'{settings.BASE_DIR}/forum/neural_net/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

def is_toxic(comment):
    sentence = comment
    sequences = tokenizer.texts_to_sequences(sentence)
    padded = pad_sequences(sequences, maxlen=100,
                            padding='post', truncating='post')
    pred_temp = model.predict(padded)
    pred = np.round(pred_temp)
    # print(pred)
    predictions = []
    for i in pred:
        predictions.append(i[0])
    return predictions
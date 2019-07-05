import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
class MultiLayerPerceptron(object):
    def __init__(self,hidden_neurons,feature_dim):
        self.model = keras.Sequential([
            Dense(hidden_neurons, activation=tf.nn.relu, input_shape=[feature_dim]),
            Dense(3, activation='softmax')
        ])
        self.model.compile(
            optimizer=tf.optimizers.Adam(),
            loss=tf.losses.SparseCategoricalCrossentropy(),
            metrics=['accuracy']
        )

    def train(self, train_set, train_label, plot):
        early_stop =keras.callbacks.EarlyStopping(monitor='val_loss', patience=50)
        history = self.model.fit(train_set, train_label, epochs=1000, verbose=0, validation_split = 0.1, callbacks=[early_stop])
        hist = pd.DataFrame(history.history)
        print(hist)
        acc_final = float(hist['val_accuracy'].tail(1))
        print()
        print('Final Accuracy on validation set: {}'.format(round(acc_final, 3)))
        if plot:
            plt.figure()
            plt.xlabel('Epoch')
            plt.ylabel('Mean Square Error]')
            plt.plot(hist['accuracy'], label='Train Error')
            plt.plot(hist['val_accuracy'], label = 'Val Error')
            plt.legend()
            plt.ylim([0,1])
            plt.show()

    def test(self,test_set,test_label):
        print(self.model.metrics_names)
        _, accuracy = self.model.evaluate(test_set, test_label)
        print('Accuracy on test set: {}'.format(round(accuracy, 3)))

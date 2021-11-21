"""
画出漂亮的confusion_matrix
"""

import matplotlib.pyplot as plt

import numpy as np

fig, axes = plt.subplots(2, 2)
key = [['TP', 'FN'], ['FP', 'TN']]
cm = np.random.random((4, 2, 2))
for cm, ax in zip(cm, axes.reshape(-1)):
    confusion = ax.matshow(cm, cmap='Blues')
    for (j, k), label in np.ndenumerate(cm):
        text = key[k][j] + ': ' + str(int(label))
        ax.text(k, j, text, ha='center', va='center')
    labelx = ['True T', 'No T']
    labely = ['Predicted T', 'Predicted No T']
    ax.set_xticklabels([''] + labelx)
    ax.set_yticklabels([''] + labely)
plt.show()

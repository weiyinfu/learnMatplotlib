import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

with PdfPages("haha.pdf") as pdf:
    for i in range(4):
        fig = plt.figure()
        for j in range(4):
            ax = fig.add_subplot(2, 2, j + 1)
            x = np.linspace(-np.pi, np.pi, 100)
            ax.plot(x, np.sin(x * (j + 1)), alpha=0.6)
        pdf.savefig(bbox_inches='tight')
    plt.close()

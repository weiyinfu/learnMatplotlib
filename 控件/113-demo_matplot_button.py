from matplotlib import pyplot as plt
from matplotlib.widgets import Button, RadioButtons
from PIL import Image
from skimage import data


def on_press(event):
    if event.inaxes is None:
        print("none")
        return
    fig = event.inaxes.figure
    ax = fig.add_subplot(122)
    img_gray = data.coins()
    ax.imshow(img_gray, cmap="gray")
    print(event.x, event.y)
    print(event)
    ax1.scatter(event.xdata, event.ydata)
    plt.axis("off")


if __name__ == "__main__":
    img = data.coins()
    fig = plt.figure()
    fig.canvas.mpl_connect("button_press_event", on_press)
    ax1 = fig.add_subplot(121)
    ax1.imshow(img)
    plt.axis("off")
    plt.show()

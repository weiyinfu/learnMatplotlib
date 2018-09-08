from matplotlib import pyplot as py
from matplotlib.widgets import Button
from skimage import data


def on_press(event):
    if event.inaxes is None:
        print("none")
        return
    fig = event.inaxes.figure
    ax = fig.add_subplot(122)
    img_gray = data.clock()
    ax.imshow(img_gray, cmap="gray")
    print(event)
    ax1.scatter(event.xdata, event.ydata)
    py.axis("off")
    fig.canvas.draw()


def button_press(event):
    print('button is pressed!')


def draw_button():
    global button  # must global
    point = py.axes([0.3, 0.03, 0.1, 0.03])
    button = Button(point, "click me")
    button.on_clicked(button_press)


if __name__ == "__main__":
    img = data.clock()
    fig = py.figure()
    draw_button()
    fig.canvas.mpl_connect("button_press_event", on_press)
    ax1 = fig.add_subplot(121)
    ax1.imshow(img)
    py.axis("off")
    py.show()

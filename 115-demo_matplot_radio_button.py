from matplotlib import pyplot as py
from matplotlib.widgets import Button, RadioButtons
from skimage import data


def button_press(event):
    print('button is pressed!')


def radio_press(label):
    print('select: ', label)
    radiobutton.set_active(0)


def draw_button():
    global button  # must global
    global radiobutton
    print('button')
    point = py.axes([0.2, 0.03, 0.1, 0.03])
    button = Button(point, "click me")
    button.on_clicked(button_press)
    point_two = py.axes([0.6, 0.03, 0.2, 0.05])
    radiobutton = RadioButtons(point_two, ("select me", "or me"))
    radiobutton.on_clicked(radio_press)


if __name__ == "__main__":
    img = data.astronaut()
    fig = py.figure()
    draw_button()
    fig.canvas.mpl_connect("button_press_event", radio_press)
    ax1 = fig.add_subplot(121)
    ax1.imshow(img)
    py.axis("off")
    py.show()

from matplotlib.widgets import RectangleSelector
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure


def line_select_callback(eclick, erelease):
    """
    Callback for line selection.

    *eclick* and *erelease* are the press and release events.
    """
    x1, y1 = eclick.xdata, eclick.ydata
    x2, y2 = erelease.xdata, erelease.ydata
    print(f"({x1:3.2f}, {y1:3.2f}) --> ({x2:3.2f}, {y2:3.2f})")
    print(f" The buttons you used were: {eclick.button} {erelease.button}")


def toggle_selector(event):
    print(' Key pressed.')
    if event.key == 't':
        if toggle_selector.RS.active:
            print(' RectangleSelector deactivated.')
            toggle_selector.RS.set_active(False)
        else:
            print(' RectangleSelector activated.')
            toggle_selector.RS.set_active(True)


fig = Figure()
ax = fig.add_subplot(111)
x = np.random.rand(24, 32)

ax.imshow(x)  # plot something
ax.set_title(
    "Click and drag to draw a rectangle.\n"
    "Press 't' to toggle the selector on and off.")

# drawtype is 'box' or 'line' or 'none'
toggle_selector.RS = RectangleSelector(ax, line_select_callback,
                                       interactive=True)
fig.canvas.mpl_connect('key_press_event', toggle_selector)

# Mostrar la figura
plt.show()

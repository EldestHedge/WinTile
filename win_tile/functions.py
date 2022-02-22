import pygetwindow as pw
import screeninfo as si


def open_windows():
    """open_windows function returns a list of all open windows"""

    exclusions = ["Program Manager", "Microsoft Text Input Application"]
    win_list = []

    windows = pw.getAllTitles()
    for i, x in enumerate(windows):
        if len(x) > 1 and x not in exclusions:
            win_list.append(x)

    return win_list


def window_resize(window1, tmp):
    """window_resize resizes a window given the name of the window to any size"""

    WIDTH = 1920  # These are hard-coded for now; change this later
    HEIGHT = 1080  # These are hard-coded for now; change this later

    win = pw.getWindowsWithTitle(window1)[0]

    win.size = (WIDTH//2, HEIGHT-40)  # HEIGHT-35 for normal sized (bottom) taskbar padding
    if tmp == 0:
        win.moveTo(0, 0)  # -7 we found to be optimal padding
    else:
        win.moveTo((WIDTH//2), 0)


def which_monitor_window(window):
    """which_monitor_window returns the (x,y) coordinates of where a window is.
    This will be used when determing on which monitor the window exists on"""

    win = pw.getWindowsWithTitle(window)[0]

    return win.topleft[0]


def monitor_list_resolution():
    """monitor_list_resolution returns all monitors widths and heights as lists with matching indexes"""
    displays = si.get_monitors()
    resolutions = []
    for display in displays:
        resolutions.append(display.width)
        # resolutions.append(display.height)

    return resolutions


if __name__ == "__main__":
    print("Do not run this file! Use run.py to call functions from this file only.")

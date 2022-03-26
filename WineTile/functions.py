import pygetwindow as pw
import screeninfo as si


# list all open window titles
def open_windows():
    exclusions = ["Program Manager", "Microsoft Text Input Application"]

    win_list = [v for k, v in enumerate(pw.getAllTitles()) if len(v) > 1 and v not in exclusions]
    return win_list


# resize window by window title
def window_resize(window1, count, POS, offset=None):
    WIDTH = 1920  # These are hard-coded for now; change this later
    HEIGHT = 1080  # These are hard-coded for now; change this later

    win = pw.getWindowsWithTitle(window1)[0]
    win.size = (WIDTH//count, HEIGHT-40)  # HEIGHT-35 for normal sized (bottom) taskbar padding

    win.moveTo(POS, 0)  # -7 we found to be optimal padding
    POS += WIDTH//count


# x coordinate of open window given window title
def which_monitor_window(window):
    win = pw.getWindowsWithTitle(window)[0]

    return win.topleft[0]


def maximization(window):
    win = pw.getWindowsWithTitle(window)[0]
    if win.isMaximized:  # if window is maximized, unmaximize it.
        win.restore()

# list of monitors widths/heights
def monitor_list_resolution():
    resolutions = [(disp.width, disp.height) for disp in si.get_monitors()]
    return resolutions


if __name__ == "__main__":
    print("Do not run this file! Use run.py to call functions from this file only.")

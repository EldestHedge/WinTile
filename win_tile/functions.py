import pygetwindow as pw


"""open_windows function returns a list of all open windows"""
def open_windows():
    exclusions = ["Program Manager", "Microsoft Text Input Application"]
    windows = pw.getAllTitles()

    win_list = []
    for i, x in enumerate(windows):
        if len(x) > 1 and x not in exclusions:
            win_list.append(x)
    return win_list


"""window_resize resizes a window given the name of the window to any size"""
def window_resize():
    WIDTH = 1920
    HEIGHT = 1080

    win = pw.getWindowsWithTitle("Notepad")[0]

    win.size = (WIDTH//2, HEIGHT)  # HEIGHT-35 for normal sized (bottom) taskbar padding
    win.moveTo(-7, 0)  # -7 we found to be optimal padding


"""which_monitor_window returns the (x,y) coordinates of where a window is.
This will be used when determing on which monitor the window exists on"""
def which_monitor_window():
    win = pw.getWindowsWithTitle("Notepad")[0]
    return win.topleft[0]


if __name__ == "__main__":
    print("Do not run this file! Use run.py to call functions from this file only.")

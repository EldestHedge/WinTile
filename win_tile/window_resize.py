import pygetwindow


WIDTH = 1920
HEIGHT = 1080

win = pygetwindow.getWindowsWithTitle("Notepad")[0]

win.size = (WIDTH//2, HEIGHT)
win.moveTo(-7, 0)  # -7 we found to be optimal padding

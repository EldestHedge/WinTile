"""Get window location using .topleft
Determine user screen size
Referencing the above determine which monitor the window is on
Resize the window on the monitor it is on"""

import pygetwindow as pw


win = pw.getWindowsWithTitle("Notepad")[0]
print(win.topleft[0])
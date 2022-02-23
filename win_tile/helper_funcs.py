import functions as fn

"""create a list of open windows coordinates. This list will be zipped"""
window_list = []
for window in fn.open_windows():
    window_list.append(fn.which_monitor_window(window))

# create list of screen resolutions (x) called resolutions
resolutions = fn.monitor_list_resolution()


# create dictionary with keys of open window names and values of their coordinates
hashed = dict(zip(fn.open_windows(), window_list))

"""Take the value (window location) and return the key (window name) for that window"""
def name_finder(val):
    for key, value in hashed.items():
        if val == value:
            return key

####################################################
"""For all open windows, determine which monitor they are on"""

for val in hashed.values():
    if val <= resolutions[0]:
        # val is hashed's value. Now we will get the hashed's key (the window name):
        fn.window_resize(name_finder(val))

    elif val <= resolutions[0] + resolutions[1]:
        # val is hashed's value. Now we will get the hashed's key (the window name):
        fn.window_resize(name_finder(val))

####################################################
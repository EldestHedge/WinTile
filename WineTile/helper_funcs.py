import functions as fn


#create a list of open windows coordinates. This list will be zipped
window_list = [fn.which_monitor_window(window) for window in fn.open_windows()]
# create list of screen resolutions (x) called resolutions
resolutions = fn.monitor_list_resolution()


# create dictionary with keys of open window names and values of their coordinates
hashed = dict(zip(fn.open_windows(), window_list))

#Take the value (window location) and return the key (window name) or that window
def name_finder(val):
    for key, value in hashed.items():
        if val == value:
            return key

count = len([wi for wi in hashed.values() if wi < resolutions[0][0] - 10])

#For all open windows, determine which monitor they are on
def size_passer(count):
    POS = 0
    for val in hashed.values():
        if val < resolutions[0][0] - 10:
            # val is hashed's value. Now we will get the hashed's key (the window name):
            fn.maximization(name_finder(val))
            fn.window_resize(name_finder(val), count, POS)
            POS += 1920//count

        elif val <= resolutions[0][0] + resolutions[1][0]:
            # val is hashed's value. Now we will get the hashed's key (the window name):
            # fn.window_resize(name_finder(val), count)
            pass



size_passer(count)
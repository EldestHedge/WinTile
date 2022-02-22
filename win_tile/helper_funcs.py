import functions as fn


def window_location_finder():
    # open_windows
    # fn.monitor_list_resolution
    value = 1920
    for i, d in enumerate(fn.monitor_list_resolution()):
        if value <= int(fn.monitor_list_resolution()[i]):
            print(i)
            break


def temp_showcase():
    for ind, wind in enumerate(fn.open_windows()):
        if fn.which_monitor_window(wind) <=1920:
            print(f"{wind} is on main")
            fn.window_resize(wind, ind)
    

def any_monitor_location_finder():
    for ind, wind in enumerate(fn.open_windows()):
        if fn.which_monitor_window(wind) <=1920:
            print(f"{wind} PRIMARY")
        elif fn.which_monitor_window(wind) <= 1920+1920:
            print(f"{wind} SECONDARY")


def sorter(wind):
    if fn.which_monitor_window(wind) < fn.monitor_list_resolution()[0]:
        print(f"{wind=} main")

    
def mon_test():
    for ind, wind in enumerate(fn.open_windows()):
        print(ind)
        sorter(wind)

    
mon_test()
# any_monitor_location_finder()
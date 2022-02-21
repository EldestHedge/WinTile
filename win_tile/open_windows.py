import pygetwindow

exclusions = ["Program Manager", "Microsoft Text Input Application"]
win_list = []
windows = pygetwindow.getAllTitles()


for i, x in enumerate(windows):
    if len(x) > 1 and x not in exclusions:
        win_list.append(x)


print(list(win_list))

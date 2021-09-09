
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
import os
from tkinter import Tk, Canvas, Entry, Button, PhotoImage
import main

ac = None
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("Sleep Timer by Elstan C")
window.geometry("683x295")
window.configure(bg = "#FFFFFF")
window.resizable(False, False)

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=295,
    width=683,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    683.0,
    295.0,
    fill="#2D4446",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: getInput(),
    relief="flat"
)
button_1.place(
    x=292.0,
    y=235.0,
    width=100.0,
    height=50.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: timerStartStop(False),
    relief="flat"
)
button_2.place(
    x=185.0,
    y=235.0,
    width=100.0,
    height=50.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: window.quit(),
    relief="flat"
)
button_3.place(
    x=399.0,
    y=235.0,
    width=100.0,
    height=50.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: setAction(button_4, "shutdown"),
    relief="flat"
)
button_4.place(
    x=593.0,
    y=101.0,
    width=75.0,
    height=33.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: setAction(button_5, "sleep"),
    relief="flat"
)
button_5.place(
    x=593.0,
    y=139.0,
    width=75.0,
    height=33.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: setAction(button_6, "restart"),
    relief="flat"
)
button_6.place(
    x=593.0,
    y=177.0,
    width=75.0,
    height=33.0
)

canvas.create_rectangle(
    204.0,
    49.0,
    479.0,
    109.0,
    fill="#C4C4C4",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    237.0,
    190.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0,
    font=("Asap Regular", 24 * -1)
)
entry_1.place(
    x=190.0,
    y=160.0,
    width=94.0,
    height=58.0
)
entry_1.insert(int(0), 0)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    341.0,
    190.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0,
    font=("Asap Regular", 24 * -1)
)
entry_2.place(
    x=294.0,
    y=160.0,
    width=94.0,
    height=58.0
)
entry_2.insert(int(0), 0)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    445.0,
    190.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0,
    font=("Asap Regular", 24 * -1)
)
entry_3.place(
    x=398.0,
    y=160.0,
    width=94.0,
    height=58.0
)
entry_3.insert(int(0), 0)

canvas.create_text(
    283.0,
    128.0,
    anchor="nw",
    text="Sleep Time",
    fill="#FFFFFF",
    font=("Asap Regular", 24 * -1)
)

canvas.create_text(
    228.0,
    220.0,
    anchor="nw",
    text="Days",
    fill="#E5E5E5",
    font=("Asap Regular", 12 * -1)
)

canvas.create_text(
    327.0,
    220.0,
    anchor="nw",
    text="Hours",
    fill="#FFFFFF",
    font=("Asap Regular", 12 * -1)
)

canvas.create_text(
    426.0,
    220.0,
    anchor="nw",
    text="Minutes",
    fill="#FFFFFF",
    font=("Asap Regular", 12 * -1)
)


def mainTimeUpdate():
    return main.getTime()


clockText = canvas.create_text(
    240.0,
    55.0,
    anchor="nw",
    text=mainTimeUpdate(),
    fill="#000000",
    font=("Roboto", 48 * -1)
)

expectedTimeDate = canvas.create_text(
    520.0,
    245.0,
    anchor="nw",
    fill="#FFFFFF",
    font=("Roboto", 15 * -1)
)
expectedTimeText = canvas.create_text(
    520.0,
    225.0,
    anchor="nw",
    fill="#FFFFFF",
    font=("Roboto", 15 * -1)
)


def setAction(item, selectedAction):
    item.config(highlightthickness=20,borderwidth=5)
    global ac
    ac = selectedAction
    print('ac', item, selectedAction, ac)


def action():
    global ac
    if ac is None:
        print("None")
    if ac == "shutdown":
        os.system('shutdown.exe /p /f')
        print("Shutdown")
    if ac == "sleep":
        print("Sleep")
        # if windows has hibernation set on it won't sleep
        os.system("shutdown.exe /h")
    if ac == "restart":
        print("Restart")
        os.system("shutdown /r /t 1")


timerStarted = False


def timerStartStop(bool):
    global timerStarted
    if bool:
        timerStarted = True
        canvas.itemconfig(expectedTimeDate,text="ETA Date: " + main.getExpectedTimeFormatted())
    else:
        timerStarted = False
        canvas.itemconfig(expectedTimeText, text="")


def getStartStop():
    return timerStarted


def getInput():
    try:
        day = int(entry_1.get())
        hour = int(entry_2.get())
        min = int(entry_3.get())
    except ValueError:
        canvas.itemconfig(expectedTimeText, text="String Error")
    try:
        if type(day) == int and type(hour) == int and type(min) == int:
            main.setTimer(day, hour, min)
            timerStartStop(True)
    except UnboundLocalError:
        canvas.itemconfig(expectedTimeText, text="String Error")


def timeLoop():
    canvas.itemconfig(clockText, text=main.getTimeFormatted())
    if getStartStop():
        canvas.itemconfig(expectedTimeText, text="ETA: " +str(main.timeUntilFormatted()))
        if main.timeCompare():
            action()
            window.quit()
    window.after(1000, timeLoop)


timeLoop()
window.mainloop()







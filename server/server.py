"""a script to print available devices."""
import bluetooth as bluetooth

nearby_devices = bluetooth.discover_devices(lookup_names=True)
print("found %d devices" % len(nearby_devices))

for addr, name in nearby_devices:
    print("  %s - %s" % (addr, name))
client = "40:4E:36:59:8D:85"




# from tkinter import
# class Window(Frame):
#
#
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.master = master
#         self.init_window()
#
#     #Creation of init_window
#     def init_window(self):
#
#         # changing the title of our master widget
#         self.master.title("GUI")
#
#         # allowing the widget to take the full space of the root window
#         self.pack(fill=BOTH, expand=1)
#
#         # creating a button instance
#         quitButton = Button(self, text="Quit", command=gethelp)
#
#         # placing the button on my window
#         quitButton.place(x=0, y=0)
#
# root = Tk()
#
# #size of the window
# root.geometry("400x300")
#
# app = Window(root)
# root.mainloop()
#
# def listen(addr):
# if __name__ == "__main__":
#     nearby_devices = bluetooth.discover_devices(lookup_names=True)
#     print("found %d devices" % len(nearby_devices))
#     app = SelectBlueView(None, nearby_devices)
#     app.title("Blue Control")
#     app.mainloop()

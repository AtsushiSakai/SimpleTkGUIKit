"""
tkinter sample

author: Atsushi Sakai
"""
import tkinter


def sample1():
    root = tkinter.Tk()
    root.title("Window title")
    root.geometry("400x300")
    img = tkinter.PhotoImage(file="icon.gif")
    root.tk.call('wm', 'iconphoto', root._w, img)
    root.mainloop()


def main():
    print(__file__ + " start!!")
    sample1()


if __name__ == '__main__':
    main()

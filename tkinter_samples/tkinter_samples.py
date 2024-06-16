"""
tkinter sample

author: Atsushi Sakai
"""
import tkinter
from idlelib.tooltip import Hovertip, OnHoverTooltipBase


def sample1():
    root = tkinter.Tk()
    root.title("Window title")
    root.geometry("400x300+1000+10")
    root.mainloop()


def sample2():
    root = tkinter.Tk()
    root.title("Status bar")
    root.geometry("300x300")
    status = tkinter.Label(root, text="Now processing..",
                           borderwidth=2, relief="groove")
    status.pack(side=tkinter.BOTTOM, fill=tkinter.X)
    root.mainloop()


def hello():
    print("hello!")


def sample3():
    class Application(tkinter.Frame):

        def __init__(self, master=None):
            super().__init__(master)
            self.pack()
            self.create_widgets()

        def create_widgets(self):
            self.hi_there = tkinter.Button(self)
            self.hi_there["text"] = "Hello World(click me)"
            self.hi_there["command"] = self.say_hi
            self.hi_there.pack(side="top")

            self.quit = tkinter.Button(
                self, text="QUIT", command=self.master.destroy)
            self.quit.pack(side="bottom")

        def say_hi(self):
            print("hi there, everyone!")

    root = tkinter.Tk()
    root.geometry("400x300")
    app = Application(master=root)
    app.mainloop()


def sample4():
    from tkinter import font
    root = tkinter.Tk()
    root.title("Label")
    root.geometry("300x300+1500+10")
    label1 = tkinter.Label(root, text="Hallo")
    label1.pack(side="top")
    font1 = font.Font(family='Helvetica', size=20, weight='bold')
    label2 = tkinter.Label(root, text="Bye", bg="blue", font=font1)
    label2.pack(side="top")
    font2 = font.Font(family='Times', size=40)
    label2 = tkinter.Label(root, text="See you", fg="red", font=font2)
    label2.pack(side="top")

    root.mainloop()


def sample5():
    root = tkinter.Tk()
    img = tkinter.PhotoImage(file='./icon.gif')
    label1 = tkinter.Label(root, image=img)
    label1.grid(row=1, column=1)
    label2 = tkinter.Label(root, image=img)
    label2.grid(row=1, column=2)
    label3 = tkinter.Label(root, image=img)
    label3.grid(row=2, column=1)
    label4 = tkinter.Label(root, image=img)
    label4.grid(row=2, column=2)
    root.mainloop()


def sample6():
    root = tkinter.Tk()
    root.title("Canvas")
    C = tkinter.Canvas(root, bg="white", height=300, width=300)
    C.create_polygon(10, 10, 50, 170, 130, 140, 180, 40, fill="red")
    C.create_line(10, 10, 200, 200, fill='black')
    C.pack()
    root.mainloop()


def sample7():
    root = tkinter.Tk()
    CheckVar1 = tkinter.IntVar()
    CheckVar2 = tkinter.IntVar()
    C1 = tkinter.Checkbutton(root, text="Music", variable=CheckVar1,
                             onvalue=1, offvalue=0, height=5,
                             width=20, )
    C2 = tkinter.Checkbutton(root, text="Video", variable=CheckVar2,
                             onvalue=1, offvalue=0, height=5,
                             width=20)
    C1.pack()
    C2.pack()
    root.mainloop()


def sample8():
    root = tkinter.Tk()
    L1 = tkinter.Label(root, text="Email")
    L1.pack(side=tkinter.LEFT)
    E1 = tkinter.Entry(root, bd=1)
    E1.pack(side=tkinter.RIGHT)
    root.mainloop()


def sample9():
    root = tkinter.Tk()
    root.title("Frame")
    frame = tkinter.Frame(root)
    frame.pack()

    bottomframe = tkinter.Frame(root)
    bottomframe.pack(side=tkinter.BOTTOM)

    redbutton = tkinter.Button(frame, text="1")
    redbutton.pack(side=tkinter.LEFT)

    greenbutton = tkinter.Button(frame, text="2")
    greenbutton.pack(side=tkinter.LEFT)

    bluebutton = tkinter.Button(frame, text="3")
    bluebutton.pack(side=tkinter.LEFT)

    blackbutton = tkinter.Button(bottomframe, text="Go")
    blackbutton.pack(side=tkinter.BOTTOM)

    root.mainloop()


def sample10():
    root = tkinter.Tk()
    root.title("Listbox")

    Lb1 = tkinter.Listbox(root, selectmode=tkinter.MULTIPLE)
    Lb1.insert(1, "TOKYO")
    Lb1.insert(2, "KYOTO")
    Lb1.insert(3, "OSAKA")
    Lb1.insert(4, "GUNMA")
    Lb1.insert(5, "GIFU")
    Lb1.insert(6, "EHIME")
    Lb1.pack()

    root.mainloop()


def sample11():
    root = tkinter.Tk()
    root.title("check button")
    root.geometry("300x300")
    mb = tkinter.Menubutton(root, text="Subjects", relief=tkinter.RAISED)
    mb.grid()
    mb.menu = tkinter.Menu(mb, tearoff=0)
    mb["menu"] = mb.menu

    Var1 = tkinter.IntVar()
    Var2 = tkinter.IntVar()
    Var3 = tkinter.IntVar()

    mb.menu.add_checkbutton(label="Math", variable=Var1)
    mb.menu.add_checkbutton(label="English", variable=Var2)
    mb.menu.add_checkbutton(label="Physics", variable=Var3)

    mb.pack()
    root.mainloop()


def sample12():
    def donothing():
        filewin = tkinter.Toplevel(root)
        button = tkinter.Button(filewin, text="Do nothing button")
        button.pack()

    root = tkinter.Tk()
    menubar = tkinter.Menu(root)
    filemenu = tkinter.Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=donothing)
    filemenu.add_command(label="Open", command=donothing)
    filemenu.add_command(label="Save", command=donothing)
    filemenu.add_command(label="Save as...", command=donothing)
    filemenu.add_command(label="Close", command=donothing)

    filemenu.add_separator()

    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    editmenu = tkinter.Menu(menubar, tearoff=0)
    editmenu.add_command(label="Undo", command=donothing)

    editmenu.add_separator()

    editmenu.add_command(label="Cut", command=donothing)
    editmenu.add_command(label="Copy", command=donothing)
    editmenu.add_command(label="Paste", command=donothing)
    editmenu.add_command(label="Delete", command=donothing)
    editmenu.add_command(label="Select All", command=donothing)

    menubar.add_cascade(label="Edit", menu=editmenu)
    helpmenu = tkinter.Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command=donothing)
    helpmenu.add_command(label="About...", command=donothing)
    menubar.add_cascade(label="Help", menu=helpmenu)

    root.config(menu=menubar)
    root.mainloop()


def sample13():
    root = tkinter.Tk()
    var = tkinter.StringVar()
    label = tkinter.Message(root, textvariable=var, relief=tkinter.RAISED)
    var.set("Hey!? How are you doing?")
    label.pack()
    root.mainloop()


def sample14():

    def sel():
        selection = "Value = " + str(var.get())
        label.config(text=selection)

    root = tkinter.Tk()
    root.title("Scale")
    var = tkinter.DoubleVar()
    scale = tkinter.Scale(root, variable=var)
    scale.pack(anchor=tkinter.CENTER)

    button = tkinter.Button(root, text="Get Scale Value", command=sel)
    button.pack(anchor=tkinter.CENTER)

    label = tkinter.Label(root)
    label.pack()

    root.mainloop()


def sample15():

    root = tkinter.Tk()

    labelframe = tkinter.LabelFrame(root, text="This is a left LabelFrame")
    labelframe.pack(side=tkinter.LEFT, fill="both", expand="yes")

    left = tkinter.Label(labelframe, text="Inside the left LabelFrame")
    left.pack()

    labelframe = tkinter.LabelFrame(root, text="This is a right LabelFrame")
    labelframe.pack(side=tkinter.RIGHT, fill="both", expand="yes")

    right = tkinter.Label(labelframe, text="Inside the right LabelFrame")
    right.pack()

    root.mainloop()


def sample16():
    from tkinter import messagebox

    top = tkinter.Tk()
    top.title("Message box")

    def hello_info():
        messagebox.showinfo("Say Hello", "Hello info")

    def hello_warning():
        messagebox.showwarning("Say Hello", "Hello warning")

    def hello_error():
        messagebox.showerror("Say Hello", "Hello error")

    def hello_question():
        messagebox.askquestion("Say Hello", "Hello question")

    def hello_cancel():
        messagebox.askokcancel("Say Hello", "Hello cancel")

    def hello_yesno():
        messagebox.askyesno("Say Hello", "Hello yesno")

    def hello_retrycancel():
        messagebox.askretrycancel("Say Hello", "Hello retrycancel")

    B1 = tkinter.Button(top, text="Hello info", command=hello_info)
    B1.pack()
    B2 = tkinter.Button(top, text="Hello warning", command=hello_warning)
    B2.pack()
    B3 = tkinter.Button(top, text="Hello error", command=hello_error)
    B3.pack()
    B4 = tkinter.Button(top, text="Hello question", command=hello_question)
    B4.pack()
    B5 = tkinter.Button(top, text="Hello cancel", command=hello_cancel)
    B5.pack()
    B6 = tkinter.Button(top, text="Hello yesno", command=hello_yesno)
    B6.pack()
    B7 = tkinter.Button(top, text="Hello retrycancel",
                        command=hello_retrycancel)
    B7.pack()

    top.mainloop()


class MyHovertip(Hovertip):
    def showcontents(self):
        label = tkinter.Label(self.tipwindow, text=self.text, justify=tkinter.LEFT,
                      foreground="black", background="#ffffe0", relief=tkinter.SOLID, borderwidth=1)
        label.pack()


def sample17():
    root = tkinter.Tk()
    L1 = tkinter.Label(root, text="Email")
    L1.pack(side=tkinter.LEFT)
    E1 = tkinter.Entry(root, bd=1)
    Hovertip(E1, text="Please enter your email address.")
    E1.pack(side=tkinter.RIGHT)
    root.mainloop()


class MyHovertip(Hovertip):
    def showcontents(self):
        label = tkinter.Label(self.tipwindow, text=self.text, justify=tkinter.LEFT,
                      foreground="black", background="#ffffe0", relief=tkinter.SOLID, borderwidth=1)
        label.pack()


def sample18():
    root = tkinter.Tk()
    L1 = tkinter.Label(root, text="Email")
    L1.pack(side=tkinter.LEFT)
    E1 = tkinter.Entry(root, bd=1)
    MyHovertip(E1, text="Please enter your email address.")
    E1.pack(side=tkinter.RIGHT)
    root.mainloop()


def main():
    print(__file__ + " start!!")
    #sample1()
    #sample2()
    # sample3()
    #sample4()
    #sample5()
    #sample6()
    #sample7()
    #sample8()
    #sample9()
    #sample10()
    #sample11()
    #sample12()
    #sample13()
    #sample14()
    #sample15()
    #sample16()
    # sample17()
    sample18()


if __name__ == '__main__':
    main()

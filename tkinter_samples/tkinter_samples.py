"""
tkinter sample

author: Atsushi Sakai
"""
import tkinter


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

            self.quit = tkinter.Button(self, text="QUIT", command=root.destroy)
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


def main():
    print(__file__ + " start!!")
    #  sample1()
    #  sample2()
    #  sample3()
    #  sample4()
    #  sample5()
    #  sample6()
    #  sample7()
    #  sample8()
    #  sample9()
    sample10()


if __name__ == '__main__':
    main()

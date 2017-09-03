#!/usr/bin/env python
# -*- coding:utf-8 -*-

#   brief:  Simple tkinter GUI kit library
#   author: Atsushi Sakai
#   Copyright (c): 2015 Atsushi Sakai
#
import tkinter
from tkinter import filedialog


def GetFilePathsWithDialog(fileTypes=[]):
    """
        Multipul File Select with dialog

        fileTypes: you can choise file extension
            ex) fileTypes=[('Excel Files', '.xlsx')]
    """
    root = tkinter.Tk()
    root.withdraw()
    filepath = filedialog.askopenfilenames(
        filetypes=fileTypes, parent=root)

    if isinstance(filepath, str):
        fileList = filepath.split(" ")
    elif isinstance(filepath, tuple):
        fileList = list(filepath)
    elif isinstance(filepath, list):
        fileList = filepath

    root.destroy()
    print(str(len(fileList)) + " files are selected")

    return fileList


def GetRadioButtonSelect(selectList, title="Select", msg=""):
    """
    Create radio button window for option selection

    title: Window name
    mag: Label of the radio button

    return (seldctedItem, selectedindex)
    """
    root = tkinter.Tk()
    root.title(title)
    val = tkinter.IntVar()
    val.set(0)

    if msg != "":
        tkinter.Label(root, text=msg).pack()

    index = 0
    for item in selectList:
        tkinter.Radiobutton(root, text=item, variable=val,
                            value=index).pack(anchor=tkinter.W)
        index += 1

    tkinter.Button(root, text="OK", fg="black", command=root.quit).pack()
    root.mainloop()
    root.destroy()

    print(selectList[val.get()] + " is selected")
    return (selectList[val.get()], val.get())


def GetListSelect(selectList, title="Select", msg=""):
    """
    Create list with selectList,
    and then return seleced string and index

    title: Window name
    mag: Label of the list

    return (seldctedItem, selectedindex)

    """
    root = tkinter.Tk()
    root.title(title)

    label = tkinter.Label(root, text=msg)
    label.pack()

    listbox = tkinter.Listbox(root)
    for i in selectList:
        listbox.insert(tkinter.END, i)
    listbox.pack()

    tkinter.Button(root, text="OK", fg="black", command=root.quit).pack()
    root.mainloop()

    selected = listbox.get(listbox.curselection())
    print(selected + " is selected")
    root.destroy()
    return (selected, selectList.index(selected))


def GetCheckButtonSelect(selectList, title="Select", msg=""):
    """
    Get selected check button options

    title: Window name
    mag: Label of the check button

    return selected dictionary
        {'sample b': False, 'sample c': False, 'sample a': False}
    """
    root = tkinter.Tk()
    root.title(title)

    label = tkinter.Label(root, text=msg)
    label.pack()

    optList = []
    for item in selectList:
        opt = tkinter.BooleanVar()
        opt.set(False)
        tkinter.Checkbutton(root, text=item, variable=opt).pack()
        optList.append(opt)

    tkinter.Button(root, text="OK", fg="black", command=root.quit).pack()
    root.mainloop()
    root.destroy()

    result = {}
    for (opt, select) in zip(optList, selectList):
        result[select] = opt.get()

    print(result)
    return result


def GetEntries(dataList, title="Select", msg=""):
    """
    Get entries of the list

    title: Window name
    mag: Label of the check button

    return data dictionary like:
    {'y': '5.0', 'x': '100', 'z': 'save'}
    """
    root = tkinter.Tk()
    root.title(title)

    label = tkinter.Label(root, text=msg)
    label.pack()

    entries = []
    for item in dataList:
        tkinter.Label(root, text=item).pack()
        entry = tkinter.Entry(root)
        entry.pack()
        entries.append(entry)

    # print entries
    tkinter.Button(root, text="OK", fg="black", command=root.quit).pack()
    root.mainloop()

    result = {}
    for (entry, data) in zip(entries, dataList):
        result[data] = entry.get()

    root.destroy()
    print(result)
    return result


if __name__ == '__main__':
    # Test
    pass

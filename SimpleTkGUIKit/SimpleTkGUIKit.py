#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   brief:  Simple Tkinter GUI kit library 
#   author: Atsushi Sakai
#   Copyright (c): 2015 Atsushi Sakai
#
import Tkinter
import tkFileDialog

class SimpleTkGUIKit:
       
    @classmethod
    def GetFilePathsWithDialog(self,fileTypes=[]):
        """
            Multipul File Select with dialog

            fileTypes: you can choise file extension
                ex) fileTypes=[('Excel Files', '.xlsx')]
        """
        root=Tkinter.Tk()
        root.withdraw()
        filepath = tkFileDialog.askopenfilenames(filetypes = fileTypes, parent=root)

        if isinstance(filepath,str):
            fileList=filepath.split(" ")
        elif isinstance(filepath,tuple):
            fileList=list(filepath)
        elif isinstance(filepath,list):
            fileList=filepath

        root.destroy()
        print str(len(fileList))+" files are selected"

        return fileList

    @classmethod
    def GetRadioButtonSelect(self, selectList, title="Select", msg=""):
        """
        Create radio button window for option selection

        title: Window name
        mag: Label of the radio button

        return (seldctedItem, selectedindex)
        """
        root = Tkinter.Tk()
        root.title(title)
        self.val = Tkinter.IntVar()
        self.val.set(0)

        if msg!="":
            Tkinter.Label(root, text=msg).pack()

        index=0
        for item in selectList:
            Tkinter.Radiobutton(root, text=item, variable=self.val, value=index).pack(anchor=Tkinter.W)
            index+=1

        Tkinter.Button(root, text="OK", fg="black", command=root.quit).pack()
        root.mainloop()
        root.destroy()

        print selectList[self.val.get()]+" is selected"
        return (selectList[self.val.get()], self.val.get())

    @classmethod
    def GetListSelect(self, selectList, title="Select", msg=""):
        """
        Create list with selectList, 
        and then return seleced string and index

        title: Window name
        mag: Label of the list

        return (seldctedItem, selectedindex)

        """
        root = Tkinter.Tk()
        root.title(title)

        label = Tkinter.Label(root,text=msg)
        label.pack()

        listbox = Tkinter.Listbox(root)
        for i in selectList:
            listbox.insert(Tkinter.END, i)
        listbox.pack()

        Tkinter.Button(root, text="OK", fg="black", command=root.quit).pack()
        root.mainloop()

        selected=listbox.get(listbox.curselection())
        print selected+" is selected" 
        root.destroy()
        return (selected,selectList.index(selected))

    @classmethod
    def GetCheckButtonSelect(self, selectList, title="Select", msg=""):
        """
        Get selected check button options

        title: Window name
        mag: Label of the check button

        return selected dictionary
            {'sample b': False, 'sample c': False, 'sample a': False}
        """
        root = Tkinter.Tk()
        root.title(title)

        label = Tkinter.Label(root,text=msg)
        label.pack()

        optList=[]
        for item in selectList:
            opt = Tkinter.BooleanVar()
            opt.set(False)
            Tkinter.Checkbutton(root, text = item, variable =opt).pack()
            optList.append(opt)

        Tkinter.Button(root, text="OK", fg="black", command=root.quit).pack()
        root.mainloop()
        root.destroy()

        result={}
        for (opt, select) in zip(optList,selectList):
            result[select]=opt.get()

        print result
        return result

    @classmethod
    def GetEntries(self, dataList, title="Select", msg=""):
        """
        Get entries of the list

        title: Window name
        mag: Label of the check button

        return data dictionary like:
        {'y': '5.0', 'x': '100', 'z': 'save'}
        """
        root = Tkinter.Tk()
        root.title(title)

        label = Tkinter.Label(root,text=msg)
        label.pack()

        entries=[]
        for item in dataList:
            Tkinter.Label(root,text=item).pack()
            entry=Tkinter.Entry(root)
            entry.pack()
            entries.append(entry)

        #print entries
        Tkinter.Button(root, text="OK", fg="black", command=root.quit).pack()
        root.mainloop()

        result={}
        for (entry, data) in zip(entries,dataList):
            result[data]=entry.get()

        root.destroy()
        print result
        return result



if __name__ == '__main__':
    #Test

    print "GetFilePathsWithDialog"
    fileList=SimpleTkGUIKit.GetFilePathsWithDialog()
    print fileList
    fileList=SimpleTkGUIKit.GetFilePathsWithDialog(fileTypes=[('CSV Files', '.csv')])
    print fileList

    print "GetRadioButtonSelect"
    (selected,index)=SimpleTkGUIKit.GetRadioButtonSelect(["sample a","sample b","sample c"])
    print selected
    (selected,index)=SimpleTkGUIKit.GetRadioButtonSelect(["Red","Green","Blue"],title="Color Select",msg="Please select color")
    print selected

    print "GetListSelect"
    (selected,index)=SimpleTkGUIKit.GetListSelect(["sample a","sample b","sample c"])
    print (selected,index)
    (selected,index)=SimpleTkGUIKit.GetListSelect(["sample a","sample b","sample c"], title="Select sample", msg="Please select sample")
    print (selected,index)

    print "GetCheckButtonSelect"
    optList=SimpleTkGUIKit.GetCheckButtonSelect(["sample a","sample b","sample c"], title="Select sample", msg="Please select sample")

    print "GetEntries"
    dataList=SimpleTkGUIKit.GetEntries(["x","y","z"], title="set entris", msg="Please set entries")
    print dataList



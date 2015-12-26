SimpleTkGUIKit
===============
Simple GUI kit with Python tkinter

# Install

# Usage

## GetFilePathsWithDialog

You can get file full-paths with file dialog.

    fileList=SimpleTkGUIKit.GetFilePathsWithDialog()
    print fileList

If you set the fileTypes, the client have to select files of the file types.

    fileList=SimpleTkGUIKit.GetFilePathsWithDialog(fileTypes=[('CSV Files', '.csv')])
    print fileList


## GetRadioButtonSelect

You can 


    (selected,index)=SimpleTkGUIKit.GetRadioButtonSelect(["sample a","sample b","sample c"])
    print selected

![radio1.png](https://github.com/AtsushiSakai/SimpleTkGUIKit/blob/master/img/radio1.png)

    (selected,index)=SimpleTkGUIKit.GetRadioButtonSelect(["Red","Green","Blue"],title="Color Select",msg="Please select color")
    print selected

![radio2.png](https://github.com/AtsushiSakai/SimpleTkGUIKit/blob/master/img/radio2.png)


## GetListSelect
    print "GetListSelect"
    (selected,index)=SimpleTkGUIKit.GetListSelect(["sample a","sample b","sample c"])
    print (selected,index)

![list1.png](https://github.com/AtsushiSakai/SimpleTkGUIKit/blob/master/img/list1.png)

    (selected,index)=SimpleTkGUIKit.GetListSelect(["sample a","sample b","sample c"], title="Select sample", msg="Please select sample")
    print (selected,index)

![list2.png](https://github.com/AtsushiSakai/SimpleTkGUIKit/blob/master/img/list2.png)


## GetCheckButtonSelect

    print "GetCheckButtonSelect"
    optList=SimpleTkGUIKit.GetCheckButtonSelect(["sample a","sample b","sample c"], title="Select sample", msg="Please select sample")

![check1.png](https://github.com/AtsushiSakai/SimpleTkGUIKit/blob/master/img/check1.png)


## GetEntries
    print "GetEntries"
    dataList=SimpleTkGUIKit.GetEntries(["x","y","z"], title="set entris", msg="Please set entries")
    print dataList

![entry.png](https://github.com/AtsushiSakai/SimpleTkGUIKit/blob/master/img/entry.png)



SimpleTkGUIKit
===============
This is a simple GUI kit with Python tkinter

It is useful for prameter configuration with GUI

# Install

> sudo pip install SimpleTkGUIKit

# Usage

All APIs can be aviable to just import it:

    from SimpleTkGUIKit import SimpleTkGUIKit 

## GetFilePathsWithDialog

You can get file full-paths with file dialog.

    fileList=SimpleTkGUIKit.GetFilePathsWithDialog()
    print fileList

If you set the fileTypes, the client have to select files of the file types.

    fileList=SimpleTkGUIKit.GetFilePathsWithDialog(fileTypes=[('CSV Files', '.csv')])
    print fileList


## GetRadioButtonSelect

You can select a option among list options with the radio button GUI:

    (selected,index)=SimpleTkGUIKit.GetRadioButtonSelect(["sample a","sample b","sample c"])
    print selected

The GUI shows up, you can choise a option.

![radio1.png](https://github.com/AtsushiSakai/SimpleTkGUIKit/blob/master/img/radio1.png)

And then, you push the OK button, get the selected option.

You also set a title and a label on the GUI


    (selected,index)=SimpleTkGUIKit.GetRadioButtonSelect(["Red","Green","Blue"],title="Color Select",msg="Please select color")
    print selected

you can see the GUI.

![radio2.png](https://github.com/AtsushiSakai/SimpleTkGUIKit/blob/master/img/radio2.png)


## GetListSelect

You can select a option with list GUI in the same way of the radio button api.

    print "GetListSelect"
    (selected,index)=SimpleTkGUIKit.GetListSelect(["sample a","sample b","sample c"])
    print (selected,index)

![list1.png](https://github.com/AtsushiSakai/SimpleTkGUIKit/blob/master/img/list1.png)

Also, there are some GUI options.

    (selected,index)=SimpleTkGUIKit.GetListSelect(["sample a","sample b","sample c"], title="Select sample", msg="Please select sample")
    print (selected,index)

![list2.png](https://github.com/AtsushiSakai/SimpleTkGUIKit/blob/master/img/list2.png)


## GetCheckButtonSelect

This is check Button selection API, so you can select multiple options.

    print "GetCheckButtonSelect"
    optList=SimpleTkGUIKit.GetCheckButtonSelect(["sample a","sample b","sample c"], title="Select sample", msg="Please select sample")

![check1.png](https://github.com/AtsushiSakai/SimpleTkGUIKit/blob/master/img/check1.png)

This API returns dictionary of the selected options.


## GetEntries

This API is used for getting some string entries.

    print "GetEntries"
    dataList=SimpleTkGUIKit.GetEntries(["x","y","z"], title="set entris", msg="Please set entries")
    print dataList

You can set arbitrary string entries with the GUI.

![entry.png](https://github.com/AtsushiSakai/SimpleTkGUIKit/blob/master/img/entry.png)

You can set number in the entry, 
    
but them you have to convert the number string to int or float.

## PyPI site

[SimpleTkGUIKit](https://pypi.python.org/pypi/SimpleTkGUIKit/)

## Licence

[MIT](https://github.com/AtsushiSakai/googleearthplot/blob/master/LICENSE)

## Author

[AtsushiSakai](http://atsushisakai.github.io/)




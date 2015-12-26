#!/usr/bin/env python
# -*- coding:utf-8 -*-

from SimpleTkGUIKit import SimpleTkGUIKit

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



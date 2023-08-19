

'''
udim tool FOR MAYA

- Reanmes a list of selected objects based on string attributes.
- This predefined attributes are editable in the UI.
- It evaluates each item in the selection to see if is a "group" or a "geo" and renames it with the proper suffix.
_____________________________________________________________________________________________________________


SCRIPT TO LOAD THIS MODULE (TO BE RUN IN MAYA)
NOTE: I need to add the custom path because I use OneDrive. This resolves maya to no been able to see the documents
folder. Thus, it can not find the scripts folder and it fails to load the module.
The path has to be appended to maya paths.
_____________________________________________________________________________________________________________

import maya.cmds as cmds
import importlib

import sys
sys.path.append('C:/Users/agust/OneDrive/01_TINTO/DOCUMENTS/GitHub/UDIM_tool')

import udim_tool
importlib.reload(udim_tool)

udim_tool

'''
import math
import maya.cmds as cmds



#_________________________________________________________________________________________
'''

# --------------------------------------window ui------------------------------------------
# Note: The tool is setup by stacking different types of layouts bellow each other.
# All layouts live under a main column layout (the first one after the creation of the window)
# The cmds.setParent('..')  line parents each layout bellow the main columnlayout. This is needed so each control
# or widget is placed in the proper layout as desired. If not, the next widget will be parented based 
# on the previous layout
#------------------------------------------------------------------------------------------------
'''
# query in which udim tile a uv is
def get_udim_currentPosition(*args):

    [maxU, maxV]=cmds.polyEvaluate(boundingBox2d=True)
    
    maxU_value1=maxU[0]
    maxU_value2=maxU[1]
    
    maxV_value1=maxV[0]
    maxV_value2=maxV[1]
    
    rounded_maxU_value1=int(math.floor(maxU_value1))
    rounded_maxU_value2=int(math.floor(maxU_value2))
    
    rounded_maxV_value1=int(math.floor(maxV_value1))
    rounded_maxV_value2=int(math.floor(maxV_value2))
    
    current_udim_tyle_location_U=rounded_maxU_value1
    current_udim_tyle_location_V=rounded_maxV_value1
    
    return(current_udim_tyle_location_U, current_udim_tyle_location_V)


def move_to_default_Udim_tile(*args):

    currentPosition=get_udim_currentPosition()
    print(currentPosition) 
   
    cmds.polyEditUV(u = currentPosition[0]*-1, v = currentPosition[1]*-1)  


# uv udim single tyle transposition
def moveUDIM_1_left(*args): 
    currentPosition=get_udim_currentPosition()
    print(currentPosition)   
    
    #cmds.polyEditUV( uValue=1, vValue=0 )  

def moveUDIM_1_right(*args):    
    cmds.polyEditUV(u = 1, v = 0)   

def moveUDIM_1_up(*args):
    print('MOVE')   
    cmds.polyEditUV(u = 0, v = 1)  

def moveUDIM_1_down(*args):
    print('MOVE')   
    cmds.polyEditUV(u = 0, v = -1)    


# uv rotation functions
def rotateUV_22(*args):
    cmds.polyEditUV( pivotU=0.5, pivotV=0.5, angle=-22.5 )


def rotateUV_45(*args):
    cmds.polyEditUV( pivotU=0.5, pivotV=0.5, angle=-45 )


def rotateUV_90(*args):
    cmds.polyEditUV( pivotU=0.5, pivotV=0.5, angle=-90 )

    
udimTool_window = 'udim tool'

# checking if the window UI exists

if cmds.window(udimTool_window, exists=True):
    cmds.deleteUI(udimTool_window)

# Setting the window variable and naming
udimTool_window = cmds.window('udim tool')


# Left side of tool and title
cmds.rowColumnLayout( numberOfColumns=2)

cmds.columnLayout()

cmds.separator(height=10)
cmds.text(label='              UV MODIFIERS')
cmds.separator(height=20)

# pane for buttons battery
cmds.rowColumnLayout( numberOfColumns=2 )

# single tyle transposition buttons
cmds.button( label='1 udim left', width = 100, command=moveUDIM_1_left)
cmds.button( label='1 udim right', width = 100, command=moveUDIM_1_right)
cmds.button( label='1 udim up', width = 100, command=moveUDIM_1_up)
cmds.button( label='1 udim down', width = 100, command=moveUDIM_1_down)


cmds.separator(height=20)
cmds.separator(height=20)

# rotation buttons
cmds.button( label='rotate 22.5', width = 100)
cmds.button( label='rotate 45', width = 100)
cmds.button( label='rotate 75', width = 100)
cmds.button( label='rotate 90', width = 100)

cmds.separator(height=20)
cmds.separator(height=20)

# scale  up buttons
cmds.button( label='+10% scale', width = 100)
cmds.button( label='+25% scale', width = 100)
cmds.button( label='+50% scale', width = 100)
cmds.button( label='+75% scale', width = 100)

cmds.separator(height=20)
cmds.separator(height=20)

# scale down buttons
cmds.button( label='-10% scale', width = 100)
cmds.button( label='-25% scale', width = 100)
cmds.button( label='-50% scale', width = 100)
cmds.button( label='-75% scale', width = 100)


cmds.setParent('..')
cmds.setParent('..')

cmds.columnLayout()

cmds.separator(height=10)
cmds.text(label='UDIM TYLE GRID SPACE')

cmds.gridLayout( numberOfColumns=10, numberOfRows=10, cellWidthHeight=(50, 50) )


cmds.button(label='1091')
cmds.button(label='1092')
cmds.button(label='1093')
cmds.button(label='1094')
cmds.button(label='1095')
cmds.button(label='1096')
cmds.button(label='1097')
cmds.button(label='1098')
cmds.button(label='1099')
cmds.button(label='1100')


cmds.button(label='1081')
cmds.button(label='1082')
cmds.button(label='1083')
cmds.button(label='1084')
cmds.button(label='1085')
cmds.button(label='1086')
cmds.button(label='1087')
cmds.button(label='1088')
cmds.button(label='1089')
cmds.button(label='1090')


cmds.button(label='1071')
cmds.button(label='1072')
cmds.button(label='1073')
cmds.button(label='1074')
cmds.button(label='1075')
cmds.button(label='1076')
cmds.button(label='1077')
cmds.button(label='1078')
cmds.button(label='1079')
cmds.button(label='1080')

cmds.button(label='1061')
cmds.button(label='1062')
cmds.button(label='1063')
cmds.button(label='1064')
cmds.button(label='1065')
cmds.button(label='1066')
cmds.button(label='1067')
cmds.button(label='1068')
cmds.button(label='1069')
cmds.button(label='1070')


cmds.button(label='1051')
cmds.button(label='1052')
cmds.button(label='1053')
cmds.button(label='1054')
cmds.button(label='1055')
cmds.button(label='1056')
cmds.button(label='1057')
cmds.button(label='1058')
cmds.button(label='1059')
cmds.button(label='1060')


cmds.button(label='1041')
cmds.button(label='1042')
cmds.button(label='1043')
cmds.button(label='1044')
cmds.button(label='1045')
cmds.button(label='1046')
cmds.button(label='1047')
cmds.button(label='1048')
cmds.button(label='1049')
cmds.button(label='1050')


cmds.button(label='1031')
cmds.button(label='1032')
cmds.button(label='1033')
cmds.button(label='1034')
cmds.button(label='1035')
cmds.button(label='1036')
cmds.button(label='1037')
cmds.button(label='1038')
cmds.button(label='1039')
cmds.button(label='1040')


cmds.button(label='1021')
cmds.button(label='1022')
cmds.button(label='1023')
cmds.button(label='1024')
cmds.button(label='1025')
cmds.button(label='1026')
cmds.button(label='1027')
cmds.button(label='1028')
cmds.button(label='1029')
cmds.button(label='1030')


cmds.button(label='1011')
cmds.button(label='1012')
cmds.button(label='1013')
cmds.button(label='1014')
cmds.button(label='1015')
cmds.button(label='1016')
cmds.button(label='1017')
cmds.button(label='1018')
cmds.button(label='1019')
cmds.button(label='1020')


cmds.button(label='1001', command=move_to_default_Udim_tile)
cmds.button(label='1002')
cmds.button(label='1003')
cmds.button(label='1004')
cmds.button(label='1005')
cmds.button(label='1006')
cmds.button(label='1007')
cmds.button(label='1008')
cmds.button(label='1009')
cmds.button(label='1010')

cmds.setParent('..')
cmds.setParent('..')


cmds.showWindow( udimTool_window )









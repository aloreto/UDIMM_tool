

'''
RENAME TOOL FOR MAYA

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
sys.path.append('C:/Users/agust/OneDrive/01_TINTO/DOCUMENTS/GitHub/rename_tool')

import rename_tool
importlib.reload(rename_tool)

rename_tool

'''

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

# Setting the window variable and naming
udimTool_window = cmds.window('Rename tool')

# checking if the window UI exists

if cmds.window(udimTool_window, exists=True):
    cmds.deleteUI(udimTool_window)

# Setting the window variable and naming
udimTool_window = cmds.window('Rename tool')

cmds.columnLayout()
cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 0), columnWidth=[(1, 100), (2, 250)] )
cmds.text( label='Name' )
name_field = cmds.textField(text='name' )
cmds.text( label='sufix_geo')
sufix_geo_field = cmds.textField(text='geo' )
cmds.text( label='sufix_group' )
sufix_group_field = cmds.textField(text='grp' )
cmds.text( label='side' )
side_field = cmds.textField(text='C' )
cmds.setParent('..')

cmds.columnLayout()
cmds.button( label='Rename', width = 350)
cmds.separator(h=30, width = 350)
cmds.text( label='Side suffix replacer', width=350, align= 'center' )
cmds.setParent('..')

cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 0), columnWidth=[(1, 175), (2, 175)] )
cmds.text( label='current side letter', width=175)
currentLetterField= cmds.textField(width=175)
cmds.setParent('..')

cmds.columnLayout()
cmds.button( label='Rename Side Letter', width = 350)
cmds.setParent('..')


cmds.showWindow( udimTool_window )









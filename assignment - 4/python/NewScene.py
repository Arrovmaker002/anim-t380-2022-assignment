import maya.standalone
import maya.cmds as cmds
import os
import sys
'''
maya.standalone.initialize()
#create new name
fullName = cmds.file( q =1, sn = 1, shn =1)
fullNamePath = cmds.file( q =1, sn = 1)
absName = os.path.dirname(fullNamePath)

noExtName = fullName.split('.')[0]
ext = fullName.split('.')[0]

splitName = noExtName.split('.')
splitName.reverse()

intVersion = int(splitName[0]) +1
strVersion = str(intVersion)
padding = strVersion.len()
if padding == 1:
    newVersion = '00' + strVersion
elif padding == 2:
    newVersion = '0' + strVersion
else:
    newVersion = strVersion
splitName.reverse()

listSize = len(splitName)
resolvedName = ''
for i in range(0, listSize-1):
    resolvedName += splitName[i] + ''
finalNamePath = absName + '/'+ resolvedName +  newVersion + '.' + ext

#check if the file exist
if cmds.file(finalNamePath, q=1, exists = 1) == 1:
    confirm = cmds.confirmDialog ( title='WARNING', message='File exist! Overwrite?', button=['Yes','No'], defaultButton='Yes', cancelButton='No', dismissString='No' )
    if confirm == 'Yes':
        print('File saved to a new version with overwrite ')
    else:
        sys.exit()
else:
    print('File saved to a new version')

#save as new version
cmds.file( rename= finalNamePath)
cmds.file( save = True)
'''
fullName = cmds.file( q =1, sn = 1, shn =1)
fullNamePath = cmds.file( q =1, sn = 1)
absName = os.path.dirname(fullNamePath)
print(absName)
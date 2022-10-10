#Import nessesary packages for python
import os

'''-------------------------------- Create the Maya Directory ----------------------------------------'''

#____Directory path to create in:
MayaPath = r"H:\Main Storage\College\Classes Current\Techincal Pipeline/anim-t380-2022-assignment/assignment - 3/asset/maya/"
#____name of new directory to create
directory = "scenes"
#____function to actually create directory
path = os.path.join(MayaPath, directory)
os.makedirs(path)
#____Printing result of directory creation
print("Directory '% s' created" % directory)



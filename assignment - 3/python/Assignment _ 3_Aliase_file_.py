#Import nessesary packages for python
import os

'''-------------------------------- Create the .alias file ----------------------------------------'''

#Create the file names and sets file location (file path to save to)
filepath = os.path.join(r"H:\Main Storage\College\Classes Current\Techincal Pipeline\anim-t380-2022-assignment\assignment - 3\etc", "asset.alias")

#Creates the file named and loctation set above.
alias = open(filepath, "w")

#write the word "alias" in the file
alias.write("asset")
alias.close()



This is an addon that contains two texture related functions.

The first function is to bake textures from blender in pbr format (for proceduraly made materials in Blender). In order for it
to work correctly the renderer must be in cycles. In addition the user must create an image texture with a new image with the resolution
1024 x 1024. Then if both the image texture and object are selected it should work properly. The files will be saved to the C drive
in folder named Textures
(C:\Textures)

The second function is to convert a pbr texture set to Unreal texture set by combining the AO, Roughness, and Mettalic maps into a singular map in the cycles shader editor and bake it back out.


Extra Credit 
Move the cursor to the center of the world, and move selected objects to the cursor location



To install the script
	Open up Blender and click on the scripting tab at the top
	Click open at the top of the code editor
	Navigate to the code location and open it
	Run by pressing the play button at the top
	On the right side of the scene, under the miscellaneous tab, you will see the UI display
	If you don't see any properties on the right side press “n” in the viewport to enable it


To install the add-on
	Open up Blender and click on Edit at the top of the screen
	Click Preferences
	Click Add-ons
	Click Install on the top bar
	Navigate to the .zip file and open it
	Then check the box of the add-on on the screen
	Now return to the main layout tab at the top
	On the right side of the scene, under the miscellaneous tab, you will see the UI
	If you don't see any properties on the right side press “n” in the viewport to enable it
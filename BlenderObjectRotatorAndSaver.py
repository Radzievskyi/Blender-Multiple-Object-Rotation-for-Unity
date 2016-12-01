#
# Mykhailo Radzievskyi
#
# Script for import objects to Unity.
# Rotate selected object around Z axis, and save every rotation as new Blender File
# In new folder what have name of current opened file
#
# Tested with Blender v2.78 and Unity 5.4.3f1 on MacOS Sierra
#
# 2016-11-30
#
# Be careful, script changing object on your scene! Do reserve copy before use.
#
# After successful finish script, you will see last created file with rotated object
#
# Script comes without warranty, use at your own risk!

import bpy
import mathutils
import os
from math import radians, pi
import shutil

#How many variation of rotation need create
numberOfCopies = 4
currentSceneName = "Scene"

def RotateAndSaveSelectedObject():
    #Get current file Path and file Name
    filepath = bpy.data.filepath
    directory = os.path.dirname(filepath)
    #print(directory)
    
    fileName = bpy.path.basename(filepath)
    fileName = os.path.splitext(fileName)[0]
    
    # Create new directory in file location folder with name of current File
    directoryForRotation = os.path.join(directory, fileName)
    # print(directoryForRotation)
    shutil.os.mkdir(directoryForRotation)
    
    #Get current Scene
    sce = bpy.data.scenes[currentSceneName]
    ob = bpy.context.scene.objects[0]
    #Checj if present Mesh object on Scene
    if (ob.type != 'MESH'):
        return
    #Remember original object Name
    baseObjectName = ob.name 

    #Calculate Rotation Angle for every itteration
    rotationIncrement = 360 / (numberOfCopies)
    #Variable for set rotation of current Object
    currentZRotation = 0
    
    for i in range(numberOfCopies):
        # Rotate and apply rotation fixing, for correct import to Unity
        bpy.context.object.rotation_euler = (pi / 2, 0, radians(rotationIncrement))
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler = (- pi / 2, 0, 0)
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        bpy.context.object.rotation_euler = (pi / 2, 0, 0)
        
        # Rename rotated object
        bpy.context.object.name = baseObjectName + "." + str(currentZRotation)
        # Create directory for keep rotation files

        # Set name for new file (Base name + rotation angle)
        newfile_name = os.path.join(directoryForRotation, fileName + "_" +  str(currentZRotation) + ".blend")
        #S ave file
        bpy.ops.wm.save_mainfile(filepath=newfile_name)
        #C alculate next rotation angle
        currentZRotation = currentZRotation + rotationIncrement
    
    # Restore original position and name of selected object    
    bpy.context.object.rotation_euler = (radians(180) / 2, 0, radians(0))
    bpy.context.object.name = baseObjectName
    return

# Run calculation
RotateAndSaveSelectedObject()
# Update scene
bpy.context.scene.update() 

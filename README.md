# Blender-Multiple-Object-Rotation-for-Unity
Python script for blender, what allow set and save .blend files with selected model rotated on different angles

Is specific script, what make selected object rotate around 360 degrees of Z axis. And result safe in separate files what can be correct import to Unity.

You must set "numberOfCopies" what show how many rotation steps do you want get.
For sample if numberOfCopies  = 2, and script will create rotation on 0 and 180 degrees;
If numberOfCopies = 3, you will get rotation on angles : 0, 120, 240 

Every rotation, script save in different blender file, and before is automatically create folder where will be kept this files.

Notice:
- Script rotate objects what will be correct open in Unity;
- Script have sense use if your scene have only one mesh object;

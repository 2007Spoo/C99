import os
import shutil
source = input("Enter source folder name:")
destination = input("Enter destination folder name:")
source = source+'/'
destination = destination+'/'

getInfo = os.listdir(source)

for file in getInfo: 
    shutil.move((source+file), destination)
import os
import shutil
source= input("ENTER SOURCE FOLDER NAME :")
destination=input("ENTER DESTINATION FOLDER NAME :")
source=source+'/'
destination=destination+'/'
f=os.listdir(source)
for file in f:
    shutil.copy((source+file),destination)
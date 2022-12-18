# Count the Number of Files and Directory
import os

APP_FOLDER = 'Your Path'
totalFiles = 0
totalDir = 0

for base, dirs, files in os.walk(APP_FOLDER):
    print('Searching in folders: ',base)
    print('Searching in files: ',files)
    for directories in dirs:
        totalDir += 1
    for Files in files:
        totalFiles += 1
        
print('Total number of files',totalFiles)
print('Total Number of directories',totalDir)     

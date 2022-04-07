import os
from pathlib import Path

SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIO": ['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}

def pickDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return 'MISC'
print(pickDirectory('.jpeg'))

def organizeDirectory():
    for item in os.scandir():
        if item.is_dir():
            continue
        file_path = Path(item)
        filetype = file_path.suffix.lower()
        directory = pickDirectory(filetype) #Creates a variable housing the list of category for each file type
        directory_path = Path(directory) #Creates a variable housing the list of filepaths for each category
        if directory_path.is_dir() != True: #Checks if filepaths indeed exist for each category in the list 'director_path'
            directory_path.mkdir() #If no file path found (as expected in this case), create a directory with that file path
        file_path.rename(directory_path.joinpath(file_path)) #For each item in 'file_path' variable, join
        # with the corresponding category file path created

organizeDirectory()


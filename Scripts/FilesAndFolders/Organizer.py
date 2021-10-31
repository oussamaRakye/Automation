import os
from pathlib import Path

# Name of the directories and the kind of files that it will contain
SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "ZIPS": ['.zip', '.rar'],
    "AUDIO": ['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4', '.skf', '.aac'],
    "IMAGES": ['.jpg','.jpeg','.png'],
    "EXES": ['.exe']
}

# Returns the category according to which subdirectory belongs, MISC if it does not belong to any
def pickDirectory(value):
    for catagory, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return catagory
    return 'MISC'

# Iterates through all elements in the directory and adds it to folder that belongs
def organizeDirectory(_path):
    path = Path(_path)
    for item in os.scandir(path):

        # Skip directories
        if item.is_dir():
            continue

        filePath = Path(item)
        fileType = filePath.suffix.lower()
        directory = pickDirectory(fileType)
        directoryPath = Path(path.joinpath(directory))

        # Create the folder if it does not exist
        if directoryPath.is_dir() == False:
            os.mkdir(directoryPath, 0o755)
        try:
            filePath.rename(directoryPath.joinpath(filePath.name))
        except:
            print(filePath)

# Path to the directory that we want to organize
organizeDirectory("C:/Users/oussa/Downloads")
import os
import shutil
from .config import *

def archive_inputs():
    destination_folder = IARCHIVE_FOLDER
    source_folder = INPUT_FOLDER
    move_files(source_folder, destination_folder)

def archive_outputs():
    destination_folder = OARCHIVE_FOLDER
    source_folder = OUTPUT_FOLDER
    move_files(source_folder, destination_folder)

def archive_jsons():
    destination_folder = JARCHIVE_FOLDER
    source_folder = JSON_OUTPUT
    move_files(source_folder, destination_folder)


def move_files(source_folder, destination_folder):
    # Ensure the source folder exists
    if not os.path.exists(source_folder):
        print(f"The source folder '{source_folder}' does not exist.")
        return

    # Ensure the destination folder exists; create it if not
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # List all files in the source folder
    files = os.listdir(source_folder)

    # Move each file to the destination folder
    for file in files:
        # skip .gitignore files
        if not file.endswith(".gitignore"):
            source_path = os.path.join(source_folder, file)
            destination_path = os.path.join(destination_folder, file)

            # Move the file
            shutil.move(source_path, destination_path)

            print(f"Moved: {source_path} -> {destination_path}")

from os import scandir, makedirs
import os.path
from shutil import move

# ! FILL IN BELOW
# Directory of the source file e.g. Windows: "C:/TestAutomation"
source_dir = "C:/TestAutomation"

# List of directories e.g. Windows: "C:/TestAutomation\\document", "C:/TestAutomation\\presentation", ...
document_dir = ""
presentation_dir = ""
music_dir = ""
image_dir = ""
video_dir = ""
unknown_dir = ""

# List of file extensions
document = ["txt", "doc", "docx", "rtf", "odt", "pdf"]
presentation = ["ppt", "pptx", "key", "odp"]
image = ["jpg", "jpeg", "png", "gif", "bmp", "tiff", "webp", "svg"]
video = ["mp4", "avi", "mkv", "mov", "wmv", "flv", "webm"]
music = ["mp3", "wav", "flac", "aac", "ogg", "wma", "m4a"]

def check_move_file(file_entry):
    # Extract the file extension
    _, file_extension = os.path.splitext(file_entry.name)
    file_extension = file_extension.lower()
    file_extension = file_extension[1:]

    # Check the destination
    if file_extension in document:
        dest_dir = document_dir
    elif file_extension in presentation:
        dest_dir = presentation_dir
    elif file_extension in image:
        dest_dir = image_dir
    elif file_extension in video:
        dest_dir = video_dir
    elif file_extension in music:
        dest_dir = music_dir
    else:
        dest_dir = unknown_dir

    # Ensure if the destination folder exists
    if not os.path.exists(dest_dir):
        print(f"Created new directory: {dest_dir}")
    os.makedirs(dest_dir, exist_ok=True)

    # Check if the file already exists in the destination folder
    destination_path = os.path.join(dest_dir, file_entry.name)

    if not os.path.exists(destination_path):
        # Move the file to the appropriate folder
        move(file_entry.path, destination_path)
        print(f"Moved {file_entry.name} to {os.path.basename(dest_dir)} folder.")
    else:
        print(f"File {file_entry.name} already exists in {os.path.basename(dest_dir)} folder. Skipped.")

def move_dir(dir_entry):
    
    dir_path = dir_entry.path

    # Check if the directory matches one of the specified directory paths
    if dir_path in [document_dir, presentation_dir, music_dir, image_dir, video_dir, unknown_dir]:
        print(f"Directory {dir_entry.name} matches one of the specified directories. Skipped.")
    else:
        # Ensure if the destination folder exists
        if not os.path.exists(unknown_dir):
            print(f"Created new directory: {unknown_dir}")        
        os.makedirs(unknown_dir, exist_ok=True)

        # Check if the file already exists in the destination folder
        destination_path = os.path.join(unknown_dir, dir_entry.name)

        if not os.path.exists(destination_path):
            # Move the file to the appropriate folder
            move(dir_entry.path, destination_path)
            print(f"Moved {dir_entry.name} to {os.path.basename(unknown_dir)} folder.")
        else:
            print(f"File {dir_entry.name} already exists in {os.path.basename(unknown_dir)} folder. Skipped.")

if __name__ == "__main__":
    with scandir(source_dir) as entries:
        for entry in entries:
            if entry.is_file():
                check_move_file(entry)
            elif entry.is_dir():
                move_dir(entry)
            else:
                print("Error. Only files and directories can be moved.")
                exit(1)
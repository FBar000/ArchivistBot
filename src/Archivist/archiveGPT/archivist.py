import os
from archiveGPT.utils import * 


def createEntryDraft(user_msg:str="Make an entry.", GPT_primer:str=None) -> str:
    entry = mkEntry(user_msg, GPT_primer)
    return toFile(entry)



def saveEntryDraft(file_path:str) -> str:
    directory = cfg.JSON_OUTPUT
    old_name = os.path.splitext(os.path.split(file_path)[-1])[0]
    e_json = fromFile(file_path)
    if "IDNO" not in e_json.keys():
        raise KeyError("Add IDNO to draft!")
    new_name = e_json["IDNO"].replace(".", ",")    
    rename_images(cfg.INPUT_FOLDER, new_name)
    rename_file(cfg.OUTPUT_FOLDER, old_name, new_name)
    file_name = os.path.join(directory, f"{new_name}.json")
    # create dir if nonexistent
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory '{directory}' was created.")
    # write to dir
    with open(file_name, "w") as file:
        json.dump(e_json, file, indent=4)
    print(f"Created: {file_name}")
    return file_name
    


def mkEntry(user_msg:str, GPT_primer:str=None, mode:str='json'):
    """
    Creates an archival record for the object with images in the 'Inputs' folder.

    Parameters:
        user_msg (str): Custom instructions by the user for a given item.
        GPT_primer (str): Instructions to the GPT on how to output its answer. NONE defaults to the instructions specified in [TODO: Add file location]
        mode (str): Controls the output of this function. Defaults to a json version of the entry. Options are ['json', 'dev']

    Returns
        json_entry (dict): a JSON-like dictionary containing the archival entry
        entry (OpenAI().chat)): the raw output from the OpenAI API client
    """
    if user_msg == None:
        raise TypeError("Function expects strings")
    if mode not in ['json', 'dev']:
        raise TypeError("Function expects mode in ['json', 'dev']")
    if GPT_primer == None:
        GPT_primer = getPrimer()
    encoded_imgs = getPhotos()
    msg = mkMessage(encoded_imgs, user_msg, GPT_primer)
    entry = mkRecords(msg)
    if mode.lower() == 'json':
        json_entry = toJSON(entry)
        return json_entry
    if mode == 'dev':
        return entry






# Code from chat GPT
def rename_images(directory_path, new_prefix):
    # Ensure the directory path is valid
    if not os.path.isdir(directory_path):
        print(f"The specified path '{directory_path}' is not a valid directory.")
        return
    # List all files in the directory
    files = os.listdir(directory_path)

    # Filter only image files (you can customize the extensions)
    image_files = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    # Rename image files
    for i, old_name in enumerate(image_files, 1):
        file_extension = os.path.splitext(old_name)[1].lower()
        new_name = f"{new_prefix}_{i}{file_extension}"

        # Construct full paths for old and new names
        old_path = os.path.join(directory_path, old_name)
        new_path = os.path.join(directory_path, new_name)

        # Rename the file
        os.rename(old_path, new_path)

        print(f"Renamed: {old_path} -> {new_path}")

# Code from chat GPT
def rename_file(directory_path, old_name, new_name):

    new_name = f'{new_name}.txt'
    old_name = f'{old_name}.txt'
    # Construct full paths for old and new names
    old_path = os.path.join(directory_path, old_name)
    new_path = os.path.join(directory_path, new_name)

    # Rename the file
    os.rename(old_path, new_path)

    print(f"Renamed: {old_path} -> {new_path}")
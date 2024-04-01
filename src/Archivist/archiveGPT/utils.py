import json
import base64
import os
import re

from openai import OpenAI
from .config import *
from .API_key import *


def getPrimer(priming_folder: str = None) -> list:
    src = PRIMING_INSTRUCTION_PATH if priming_folder == None else priming_folder
    res = ""
    for filename in os.listdir(src):
        file_path = os.path.join(src, filename)
        if os.path.isfile(file_path) and filename.endswith('.txt'):
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                res += content + '\n'
    return {
        "role": "system",
        "content": [{"type": "text", "text": res}]
    }


def getPhotos() -> list:
    paths = get_images_path(INPUT_FOLDER)
    encd_imgs = encode_images(paths)
    return encd_imgs


def get_images_path(folder_path):
    return [os.path.join(folder_path, i) for i in os.listdir(folder_path) if i.endswith('.png')]


# Encode many images
def encode_images(image_paths) -> list:
  encoded_imgs = list()
  for image_path in image_paths:
    encoded_imgs.append(__encode_image(image_path))
  return encoded_imgs


# Aux function to encode an image
def __encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')


def mkMessage(encoded_images, user_query_content, GPT_primer=None) -> str:
    content = [
        {"type": "text", "text": user_query_content}
    ]
    for img in encoded_images:
        tmp = __image_upload(f"data:image/jpeg;base64,{img}")
        content.append(tmp)
    
    query = {
        "role": "user",
        "content": content
    }
    message = [GPT_primer, query] if GPT_primer != None else [query]
    return message

    
# Aux function thatspecifies the message to upload an image from url to api
def __image_upload(img_url):
    return {
          "type": "image_url",
          "image_url": {
            "url": img_url
          }}



def mkRecords(msg: str) -> OpenAI:
    client = OpenAI(api_key=API_KEY)
    response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=msg,
    max_tokens=500,
    )
    return response



def toJSON(response: OpenAI) -> dict:
    reply_str_json = re.findall("{[\s\S]*}", response.choices[0].message.content)
    return json.loads(reply_str_json[0], strict=False)



## From ChatGPT
def fromFile(file_path: str) -> dict:
    # Initialize an empty dictionary
    entry = {}
    # Temporary variables to hold the current key and value
    current_key = None
    current_value = []

    # Open the file for reading
    with open(file_path, 'r') as file:
        for line in file:
            # Check if the line is a key (all caps)
            if line.strip().isupper():
                # If there's an existing key, save its value
                if current_key is not None:
                    entry[current_key] = '\n'.join(current_value).strip()
                # Update the current key and reset the value
                current_key = line.strip()
                current_value = []
            else:
                # Accumulate the value
                current_value.append(line)

        # Add the last key-value pair to the dictionary
        if current_key is not None:
            entry[current_key] = '\n'.join(current_value).strip()

    return entry


def toFile(entry: dict, count=0):
    file_path = os.path.join(OUTPUT_FOLDER, f"{count}.txt")
    # Open a file for writing or create it if it doesn't exist
    with open(file_path, 'w') as file:
        for key, value in entry.items():
            file.write(key+"\n")
            file.write(value+2*"\n")
    return file_path


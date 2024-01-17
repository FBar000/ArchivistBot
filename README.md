# ArchivistBot

This is a tool that uses OpenAI's chatbot with vision to facilitate the archiving of historical documents on the Collective Access database. Users provide photographs of historical documents and brief descriptions and this program creates the corresponding digital record with metadata(e.g. date, content scope and summary, condition).

## Installation & Set-up

There are three steps to setting up this tool:
1. Installing the necessary software 
2. Registering an API key and adding it to ArchivistBot
3. Adding your CollectiveAccess login credentials to ArchivistBot

You will need to go into the `archiveGPT` and `bots` folders to add variables as part of the initial configuration. After initial setup, you will be interacting with the `Stage`, `Archive`, and `Archivist.ipynb` files alone*. The rest simply house function definitions and variable names. 

*The `Useful Functions` folder contains additional files which may be useful for certain tasks, like automating set creation on Collective Access, but those 

### Software Installation

As of January 2024, this tool requires an IDE (e.g. VS Code) and Jupyter Notebook. Installation instructions can be found on those webpages.

Once that software is installed, install this tool via

```bash
$ git clone https://github.com/FBar000/ArchivistBot.git
```

Then install dependencies in the project's virtual environment: 

```bash
$ pip install -r requirements.txt
```

### API Setup

To use the OpenAI API, you must first create an account on OpenAI, fund it, and register an API key. Follow their instructions to do this.

Once you have the API key, paste it in the `API_KEY` variable in `archiveGPT/config.py`.

```python
API_KEY = r'' ## Include your API Key
```

At this point, you have all you need to generate archival entries, but note that these cannot yet be uploaded to CollectiveAccess (see next step).

### CollectiveAccess Interface Set-up

To allow `ArchivistBot` to access CollectiveAccess, add the username and password that you use to log onto the database into the `CREDENTIALS` dictionary in the `configs.py` file in the `bots` package:

```python
CREDENTIALS = {
    "username": "",
    "password": ""
} 
```

If you are not accessing the Madison Historical Society's CollectiveAccess backend, you will need to also update the `URLS` variable and possibly the XPaths*


*I do not know if all CollectiveAccess pages are structured identically. 

## Usage

The program is used at the `Archivist.ipynb` notebook and the `Stage` folder. 
* The `Archivist.ipynb` will call and execute functions
* The `Stage` folder will hold the files created and handled during usage sessions

There are three main steps in the usage of `ArchivistBot`:
1. Acquire document images
2. Process the images
3. Upload the products of step (2) to CollectiveAccess

These will be illustrated with an example. 

### Step 1: Acquire document images

Start by getting pictures of your historical documents to your computer.

#### 1.1 Take the Pictures

You must first take pictures of you historical documents and transfer these to your computer. These must be JPEG files. There is no 'right' way to take the picture, but follow the rule that any you take should be clear and complete enough for anyone who sees them to write an archival entry like the one you want. 

#### 1.2 Transfer them to your Computer

Transfer the images to your computer using your preferred method but note that your choice matters. For instance, emailing large images is slow. Personally, WhatsApp'ing myself the photos and accessing the chat from my browser was a quick and reliable method.

Store the files where you will not forget them.


### Step 2: Process Images

Then, one document at a time, you will generate and control the quality of accession records. You will be executing the cells in the `"Process Images"` section of the `Archivist.ipynb` notebook.

#### 2.1: Stage the Files & Provide Additional Information

Store the images of the document under consideration in the `Stage/Inputs` folder. The ArchivistBot will always look in that folder for input.

Then, in the notebook, under `"Make Entries"`, set the `user_msg` variable to a brief description of the item, including the physical dimensions. Remember to execute the cell once your message is complete.

#### 2.2: Generate a Record

Execute the next cell. This will create a draft for an accession record based off the images and your description. It will appear as a file named `0.txt` in the `Stage/Output` folder. 

#### 2.3: Complete the Draft

Read the newly created file to ensure a quality response. If you are unhappy with the result, there are two options:
1. *Manually correct the file.* Simply edit the file as you would a regular text file. You can do this for minor fixes, such as to correct spelling. Remember to save.
2. *Rerun Steps 2.1 and 2.2.* Treat the program as you would an employee. Delete the file, provide more detailed instructions, and have it generate another record. Repeat Step 2.3.

Once you are happy with the result, you must add an `IDNO` value to the start of the record. Follow your museum's standards and conventions. Here is an example:

```txt
IDNO
A2024.Test.000

TITLE
...
```

#### Step 2.4: Cleanup

Run the next cell to 
1. Rename the images and the corrected draft file according to the IDNO you provided, for later reference
2. Move the renamed images and draft to the `Archive` folder (`Archive/Inputs` and `Archive/Outputs`)
3. Create a JSON file from the corrected draft

### Step 3: Upload to Collective Access

## Developer Guide
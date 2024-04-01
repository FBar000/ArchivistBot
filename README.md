# ArchivistBot

This is a tool that uses OpenAI's chatbot with vision to facilitate the archiving of historical documents on a [Collective Access](https://www.collectiveaccess.org/) database. Users provide photographs and brief descriptions of historical documents and this program creates the corresponding digital record (e.g. date, content scope and summary, condition).

## Installation & Set-up

There are three steps to setting up this tool:
1. Instal the necessary software 
2. [Create an OpenAI account, register an  API key](https://platform.openai.com/docs/quickstart?context=python), and add it to ArchivistBot
3. Add your CollectiveAccess login credentials to ArchivistBot

You will need to go into the `archiveGPT` and `bots` folders to add variables as part of the initial configuration. After initial setup, you will be interacting with the `Stage`, `Archive`, and `Archivist.ipynb` files alone*. The rest simply house function definitions and variable names. 

*The `Useful Functions` folder contains additional files which may be useful for certain tasks, like automating set creation on Collective Access.

### Installation

As of January 2024, this tool requires an IDE (e.g. [VS Code](https://code.visualstudio.com/)) and [Jupyter Notebook](https://code.visualstudio.com/docs/datascience/jupyter-notebooks). Installation instructions can be found on those webpages.

Once that software is installed, install this tool via

```bash
git clone https://github.com/FBar000/ArchivistBot.git
```

Then install dependencies in the project's virtual environment: 

```bash
pip install -r requirements.txt
```

### OpenAI API Setup

[To use the OpenAI API, you must first create an account on OpenAI, fund it, and register an API key.](https://platform.openai.com/docs/quickstart?context=python) 

Once you have the API key, paste it in the `API_KEY` variable in a new file `archiveGPT/API_key.py`.

```python
API_KEY = r'' ## Include your API Key
```

At this point, you have all you need to generate archival entries, but note that these cannot yet be uploaded to CollectiveAccess (see next step).

### Selenium Webbrowser

As of March 2024, this program uses [Selenium](https://selenium-python.readthedocs.io/) to interact with the databases. Follow the tool's [installation instructions](https://selenium-python.readthedocs.io/installation.html).


### CollectiveAccess Credentials Set-up

To allow `ArchivistBot` to access CollectiveAccess, add the username and password that you use to log onto the database into the `CREDENTIALS` dictionary in a new file `bots/creds.py`:

```python
CREDENTIALS = {
    "username": "",
    "password": ""
} 
```


(I do not know if all CollectiveAccess pages are structured identically. In the case that they aren't, you will need to modify the XML paths specified in `configs.py` of the bots module.)


## Usage

Users interact with the `Archivist.ipynb` notebook and the `Stage` folder. 
* The `Archivist.ipynb` is the command center that coordinates all the functions
* The `Stage` folder holds the files created and handled during sessions

There are three steps to using this program: 
1. Acquire document images
2. Process the images
3. Upload the results to CollectiveAccess


### Step 1: Acquire document images

Begin by getting pictures of your historical documents to your computer.

#### 1.1 Take the Pictures

First take pictures of you historical documents. These must be JPEG files. Any you take should be clear and complete enough for anyone who sees them to write an archival entry like the one you want. 

#### 1.2 Transfer them to your Computer

Transfer the images to your computer using your preferred method. Your choice matters and may lead to bottlenecks: for instance, emailing large images is slow. Personally, [WhatsApp](https://www.whatsapp.com/)'ing myself the photos from my phone and accessing the chat from my browser was a quick and reliable method.

Store the files where you will not forget them.


### Step 2: Process Images

Next, one document at a time, you will generate and control the quality of accession records. You will be executing the cells in the `"Process Images"` section of the `Archivist.ipynb` notebook. Iterate for each document: 

#### 2.1: Stage the Files & Provide Additional Information

Store the images of the document under consideration in the `Stage/Inputs` folder. The ArchivistBot will always look in that folder for input.

In the notebook, under `"Make Entries"`, set the `user_msg` variable to a brief description of the item, including the physical dimensions. Remember to execute the cell once your message is complete to store it to memory.

#### 2.2: Generate a Record

Execute the next cell. This will create a draft for an accession record based off the images and your description. It will appear as a file named `0.txt` in the `Stage/Output` folder. 

#### 2.3: Complete the Draft

Read the newly created file to ensure a quality response. If you are unhappy with the result, there are two options:
1. *Manually correct the file.* Simply edit the file as you would a regular text file. You can do this for minor fixes, such as to correct spelling. Remember to save.
2. *Rerun Steps 2.1 and 2.2.* Delete the file, provide more detailed instructions in the `user_msg`, and repeat Step 2.2.

Once you are happy with the result, you must add an `IDNO` value to the start of the record. Follow your museum's standards and conventions. 
#### Here is an example for an organization that uses the convention `AXXXX.DESC.YYY` where `XXXX` is the accession year, `DESC` is a category, and `YYY` is a unique identifier within the category:

```txt
IDNO
A2024.Test.000

TITLE
Book - "Journey to the Center of the Earth"

...[etc.]
```

#### Step 2.4: Save and Cleanup

Run the next cell to 
1. Rename the images and the corrected draft file according to the `IDNO` you provided, for later reference
2. Create a JSON file from the corrected draft
3. Move the renamed images and draft to the `Archive` folder (`Archive/Inputs` and `Archive/Outputs`)


### Step 3: Upload to Collective Access

To upload the JSONs to Collective Access, run the two cells under the header "Upload to CTCo"

The first cell will create a list variable with the paths to the files. The second cell will open a selenium websession and iterate over the list, creating an object according to each set of instructions in the JSONs. 

### Step 4: Archive JSONs

Run the final cell to move the processed JSON instructions from the `Stage` folder to the `Archive` folder, where you may access them later.


## Developer Guide
# ArchivistBot

This is a tool that uses OpenAI's gpt-4-vision-preview model to facilitate the archiving of historical documents on the Collective Access database. Users provide photographs of historical documents and brief descriptions and this program creates the corresponding digital record with metadata(e.g. date, content scope and summary, condition).

## Installation & Set-up

There are three steps to setting up this tool:
1. Installing the necessary software 
2. Registering an API key and adding it to ArchivistBot
3. Adding your CollectiveAccess login credentials to ArchivistBot

You will need to go into the `archiveGPT` and `bots` folders to add variables as part of the initial configuration. After initial setup, you will be interacting with the `Stage`, `Archive`, and `Archivist.ipynb` files alone*. The rest simply house function definitions and variable names. 

### Software Installation

As of January 2024, this tool requires an IDE (e.g. VS Code) and Jupyter Notebook. Installation instructions can be found on those webpages.

Once that software is installed, install this tool via

```
$ git clone https://github.com/FBar000/ArchivistBot.git
```

Then install dependencies in the project's virtual environment: 

```
$ pip install -r requirements.txt
```

### API Setup

To use the OpenAI API, you must first create an account on OpenAI, fund it, and register an API key. Follow their instructions to do this.

Once you have the API key, paste it in the `API_KEY` variable in `archiveGPT/config.py`.

```
API_KEY = r'' ## Include your API Key
```

At this point, you have all you need to generate archival entries, but note that these cannot yet be uploaded to CollectiveAccess (see next step).

### CollectiveAccess Interface Set-up

To allow `ArchivistBot` to access CollectiveAccess, add the username and password that you use to log onto the database into the `CREDENTIALS` dictionary in the `configs.py` file in the `bots` package:

```
CREDENTIALS = {
    "username": "",
    "password": ""
} 
```

If you are not accessing the Madison Historical Society's CollectiveAccess backend, you will need to also update the `URLS` variable and possibly the XPaths*


*I do not know if all CollectiveAccess pages are structured identically. 

## Usage

The program is used at the `Stage` folder and the `Archivist.ipynb` notebook. You will be interacting with files alone.

There are three main steps in the usage of `ArchivistBot`:
1. Acquire document images
2. Process the images
3. Upload the products of step (2) to CollectiveAccess

 
The first step requires you take photographs of the document you want to catalog and transfer these to the `Stage/Input` file. 

These will be illustrated with an example: 

## Developer Guide

CREDENTIALS = {
    "username": "",
    "password": ""
} ## Add your CTCo Credentials

# CTCo Variables

URLS= {
    "LOGIN_URL":  r"",
    "NEWDOC_URL": r'',
    "SEARCH_BUILDER": r''
}



LOGIN_XPATHS = {
    "username": '//*[@id="login"]/div[1]/input',
    "password": '//*[@id="login"]/div[2]/input',
    "submit": ' //*[@id="login"]/div[3]/a'
}

DOC_MENU_XPATHS = {
    "BASIC INFORMATION": '//*[@id="nav_screen_40"]',
    "PHYSICAL CHARACTERISTICS": '//*[@id="nav_screen_41"]',
    "CONDITION": '//*[@id="nav_screen_47"]',
    "Save" : '//*[@aria-label="Save"]'
}

DOC_XPATHS = {
    "idno": '//*[@id="idno_accession_number"]',
    "title": '//*[@id="P732ObjectEditorForm_Prefname_new_0"]',
    "date value": '//*[@id="P735ObjectEditorForm_attribute_56_57_new_0"]',
    "date type": '//*[@id="P735ObjectEditorForm_attribute_56_58_new_0"]', 
    "curatorial desc": '//*[@id="cke_1_contents"]/iframe'
}

DOC_PHYS_XPATHS = {
    "height": '//*[@id="P742ObjectEditorForm_attribute_36_37_new_0"]',
    "width": '//*[@id="P742ObjectEditorForm_attribute_36_38_new_0"]',
    "measurement notes": '//*[@id="P742ObjectEditorForm_attribute_36_45_new_0"]'
}

DOC_COND_XPATHS = {
    'condition notes': '(//textarea)[2]'
}


DATE_TYPE_CODES = {
            "Date accepted": 182,
            "Date collected": 185,
            "Date copyrighted": 184,
            "Date manufactured/created": 187,
            "Date of alteration": 188,
            "Date published": 183,
            "Earliest/Latest dates": 186,
            "Patent date": 189}


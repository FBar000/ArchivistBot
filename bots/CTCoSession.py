from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


import bots.configs as cfg

class CTCoSession(webdriver.Chrome):

    def __init__(self):
        super().__init__()
        self.get(cfg.URLS["LOGIN_URL"])
        self.__wait_until(cfg.LOGIN_XPATHS["username"]).send_keys(cfg.CREDENTIALS["username"])
        self.__wait_until(cfg.LOGIN_XPATHS["password"]).send_keys(cfg.CREDENTIALS["password"])
        self.__wait_until(cfg.LOGIN_XPATHS["submit"]).click()


    def create_object(self, doc):
        self.get(cfg.URLS["NEWDOC_URL"])
        self.__write_basic_info(doc)
        self.__write_physical(doc)
        self.__write_condition(doc)
        return ""

    def __write_basic_info(self, doc):
        # Precondition: Browser on newdoc_url
        self.__input_values(cfg.DOC_XPATHS["idno"], doc["IDNO"])
        self.__input_values(cfg.DOC_XPATHS["title"], doc["TITLE"])
        self.__input_values(cfg.DOC_XPATHS["date value"], doc["DATE VALUE"])
        self.__make_curatorial_desc(doc)
        self.__save_page()

    def __write_physical(self, doc):
        # Precondition: Browser on object's page
        self.__wait_until(cfg.DOC_MENU_XPATHS["PHYSICAL CHARACTERISTICS"]).click()
        self.__input_values(cfg.DOC_PHYS_XPATHS['height'], doc['HEIGHT'])
        self.__input_values(cfg.DOC_PHYS_XPATHS['width'], doc['WIDTH'])
        self.__input_values(cfg.DOC_PHYS_XPATHS['measurement notes'], doc['MEASUREMENT NOTES'])
        # TODO: Add measurement notes?
        # TODO: Test SAVING functionality
        self.__save_page()

    def __write_condition(self, doc):
        # Precondition: Browser on object's page
        self.__wait_until(cfg.DOC_MENU_XPATHS["CONDITION"]).click()
        self.__input_values(cfg.DOC_COND_XPATHS['condition notes'], doc['CONDITION REPORT'])
        self.__save_page()

    def __make_curatorial_desc(self, doc):
        source_mode_button_xpath = '//*[@id="cke_38"]'
        content_xpath = '//*[@id="cke_1_contents"]/textarea'
        self.__wait_until(source_mode_button_xpath).click()
        self.__input_values(content_xpath, doc["CURATORIAL DESCRIPTION"])


    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def __wait_until(self, x_path_str): return WebDriverWait(self, 15).until(lambda x: x.find_element(By.XPATH, x_path_str))

    def __save_page(self): 
        ele = self.__wait_until(cfg.DOC_MENU_XPATHS["Save"])
        self.execute_script("arguments[0].click();", ele)

    def __input_values(self, input_field_XPATH, value, save_page=False):
        ele = self.__wait_until(input_field_XPATH)
        ele.clear()
        ele.send_keys(value)
        if save_page: self.__save_page()
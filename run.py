#!/usr/bin/env python
# -*- coding: utf-8 -*-
''

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import time
import logging


class dataSearch():
    """def construct"""

    def __init__(self):
        self.fp = webdriver.FirefoxProfile()
        self.browser = webdriver.Firefox(firefox_profile=self.fp)
        self.browser.set_window_size(1068, 1050)

    def __getEquipamentsLinks(self):
        self.browser.get(
            "http://cnes2.datasus.gov.br/Mod_Ind_Equipamento.asp?VEstado=31")
        self.all_spans = self.browser.find_elements_by_xpath(
            "//div[@class='search-result__wrapper']")
        try:

            self.url = self.browser.find_elements_by_xpath(
                "//a[@href]")  # //a[@href] Procura LINK
        except NoSuchElementException:
            print("erro to find element")

        # Get DIV
        for self.span in self.all_spans:
            print self.span.text

    def run(self):
        self.__getEquipamentsLinks()


def main():
    obj = dataSearch()
    obj.run()

if __name__ == '__main__':
    main() 

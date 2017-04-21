import os
import platform

from selenium import webdriver

dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path_webdriver = os.path.join(dir_path, '../driver/')

OS_MAP = {
    '64bit': {
        '': 'mac64',
        'WindowsPE': 'win64'
    },
    '32bit': {
        'WindowsPE': 'win32'
    }
}


def getBrowser(dev=False):
    arch = platform.architecture()
    driver_path = os.path.join(dir_path_webdriver, OS_MAP[arch[0]][arch[1]])
    if dev:
        return webdriver.Chrome(os.path.join(driver_path, 'chromedriver'))
    else:
        return webdriver.PhantomJS(os.path.join(driver_path, 'phantomjs'))

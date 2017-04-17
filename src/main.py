import os

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from UPassExceptions import CredentialsNotFound, NothingToRenew, InvalidCredentials
from encryption import login_credentials

dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path_webdriver = os.path.join(dir_path, '../lib/')


def choose_school(school_name, user=None, password=None, dev=False):
    if user is None or password is None:
        raise CredentialsNotFound("Username and Password Not Found")
    if dev:
        browser = webdriver.Chrome(os.path.join(dir_path_webdriver, 'chromedriver'))
    else:
        browser = webdriver.PhantomJS(os.path.join(dir_path_webdriver, 'phantomjs'))
    browser.get("https://upassbc.translink.ca/")
    print browser.current_url
    el = browser.find_element_by_id("PsiId")
    for option in el.find_elements_by_tag_name('option'):
        if option.text == school_name:
            option.click()  # select() in earlier versions of webdriver
            break
    login_ubc(browser, user, password)


def login_ubc(browser, user, password):
    browser.find_element_by_id("goButton").click()
    print browser.current_url
    browser.find_element_by_id('j_username').send_keys(user)
    browser.find_element_by_id('password').send_keys(password)
    browser.find_element_by_name('action').click()
    if "https://upassbc.translink.ca" not in str(browser.current_url):
        raise InvalidCredentials
    renew_upass(browser)


def renew_upass(browser):
    foo = browser.find_element_by_xpath('//*[@id="form-request"]')
    print foo.find_element_by_xpath('//*[@id="AccountStatus"]').get_attribute('value')
    print foo.find_element_by_xpath('//*[@id="Card_CardNumber"]').get_attribute('value')
    try:
        foo.find_element_by_xpath('//*[@id="chk_1"]')
    except NoSuchElementException:
        raise NothingToRenew
    foo.find_element_by_xpath('//*[@id="chk_1"]').click()
    foo.find_element_by_xpath('//*[@id="requestButton"]').click()
    print "UPass Renewed"
    browser.quit()


def main():
    user, password = login_credentials()
    try:
        choose_school("University of British Columbia", user, password, False)
    except NoSuchElementException, e:
        print "Ran into an error!\n {}".format(str(e))
    except InvalidCredentials, e:
        print "Invalid Credentials for {}".format(e.user)
    except NothingToRenew:
        print "UPass is already renewed"
    except CredentialsNotFound, e:
        print e.msg


if __name__ == '__main__':
    main()

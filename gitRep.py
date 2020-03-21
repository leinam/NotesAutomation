from selenium import webdriver
import sys
import clipboard

browser = webdriver.Chrome('/Users/Leina/Documents/PythonProgramming/NotesAutomation/chromedriver')

browser.get("https://github.com/login")


def auto_git():
    python_username_field = browser.find_element_by_xpath('//*[@id="login_field"]')
    python_pass_field = browser.find_element_by_xpath('//*[@id="password"]')
    python_login_button = browser.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[9]')

    python_pass_field.send_keys("")
    python_username_field.send_keys("leinam")
    python_login_button.click()

    python_new_repo = browser.find_element_by_xpath('/html/body/div[4]/div/aside[1]/div[2]/div[1]/div/h2/a')
    python_new_repo.click()

    python_repo_name = browser.find_element_by_xpath('//*[@id="repository_name"]')

    python_repo_name.click()
    # python_repo_name.send_keys("NewReposit")
    python_repo_name.sendkeys(sys.argv[1])

    python_create_button = browser.find_element_by_xpath('//*[@id="new_repository"]/div[3]/button')
    python_create_button.submit()

    browser.find_element_by_xpath('//*[@id="js-repo-pjax-container"]/div[3]/div/div[1]/div[1]/div/div[3]/div/span/span/clipboard-copy').click()
    remote_url = clipboard.paste()
    print(remote_url)

    return remote_url


auto_git()


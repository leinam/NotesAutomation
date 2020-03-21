from selenium import webdriver
import sys
import clipboard

browser = webdriver.Chrome('/Users/Leina/Documents/PythonProgramming/NotesAutomation/chromedriver')

# navigate to github.com
browser.get("https://github.com/login")


def auto_git():
    # find username, password fields and login button elements on page
    username_field = browser.find_element_by_xpath('//*[@id="login_field"]')
    pass_field = browser.find_element_by_xpath('//*[@id="password"]')
    login_button = browser.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[9]')

    # enter credentials and log in
    pass_field.send_keys("my_pass")
    username_field.send_keys("leinam")
    login_button.click()

    # find new repository button and click it
    new_repo = browser.find_element_by_xpath('/html/body/div[4]/div/aside[1]/div[2]/div[1]/div/h2/a')
    new_repo.click()

    # find new repository name field
    repo_name = browser.find_element_by_xpath('//*[@id="repository_name"]')

    # enter repository name
    repo_name.click()
    repo_name.send_keys(sys.argv[1])

    # create new repo with default settings
    create_button = browser.find_element_by_xpath('//*[@id="new_repository"]/div[3]/button')
    create_button.submit()

    # find button to copy remote repo URL to clipboard and click it
    browser.find_element_by_xpath('//*[@id="js-repo-pjax-container"]/div[3]/div/div[1]/div[1]/div/div[3]/div/span/span/clipboard-copy').click()

    remote_url = clipboard.paste()

    print(remote_url)

    # return remote_url


auto_git()


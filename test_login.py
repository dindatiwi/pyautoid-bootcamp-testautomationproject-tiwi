import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get('https://pandu.kominfo.go.id/login')
    driver.implicitly_wait(5)
    driver.minimize_window()
    yield driver
    driver.close()

def test_login_success(setup): #testcase 001
    setup.find_element_by_name('email').send_keys('your registered email here')
    setup.find_element_by_name('password').send_keys('your registered password here')
    setup.find_element_by_xpath('/html/body/div[3]/div/form/button').click()
    Badge = setup.find_element_by_class_name('username').text
    assert Badge == 'Your registered Name Here'
    print(Badge)

Accounts = [('your registered email here','wrong password'),
            ('wrong email','your registered password here'),
            ('wrong email','wrong password')]

@pytest.mark.parametrize('email,password', Accounts)
def test_login_unsuccess(setup,email,password): #testcase 002,003,004
    setup.find_element_by_name('email').send_keys(email)
    setup.find_element_by_name('password').send_keys(password)
    setup.find_element_by_xpath('/html/body/div[3]/div/form/button').click()
    element = setup.find_element_by_xpath('/html/body/div[3]/div/form/div[2]')
    WebDriverWait(setup,5).until(EC.visibility_of(element))
    Alert = element.is_displayed()
    assert Alert == True
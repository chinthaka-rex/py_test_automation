from selenium import webdriver

# Elements

by_id = "id"
by_xpath = "xpath"
username_id = "userName"
email_id = "userEmail"
c_add_id = "currentAddress"
p_add_id = "permanentAddress"
sub_btn_id = "submit"
uname_id = "name"
email_v_id = "email"
c_add_xpath = "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[6]/div/p[3]"
p_add_xpath = "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[6]/div/p[4]"


# Functions

def browser_load(context):
    context.driver = webdriver.Chrome(executable_path='drivers/chromedriver')
    return None


def navigate_to_the_demoqa_text_page(context, web_add):
    context.driver.get(web_add)
    return None


def enter_the_fullname(context, fuName):
    context.driver.find_element(by_id, username_id).send_keys(fuName)
    return None


def enter_email(context, email):
    context.driver.find_element(by_id, email_id).send_keys(email)
    return None


def enter_current_address(context, cAddress):
    context.driver.find_element(by_id, c_add_id).send_keys(cAddress)
    return None


def enter_permanent_address(context, pAddress):
    context.driver.find_element(by_id, p_add_id).send_keys(pAddress)
    return None


def click_submit_btn(context):
    context.driver.find_element(by_id, sub_btn_id).click()
    return None


def verify_the_name(context):
    name_text = context.driver.find_element(by_id, uname_id).text
    rt_name = name_text.split(':')
    return rt_name[1]


def verify_the_email(context):
    email_text = context.driver.find_element(by_id, email_v_id).text
    rt_email = email_text.split(':')
    return rt_email[1]


def verify_the_c_address(context):
    c_add_text = context.driver.find_element(by_xpath, c_add_xpath).text
    rt_c_add = c_add_text.split(':')
    return rt_c_add[1]


def verify_the_p_address(context):
    p_add_text = context.driver.find_element(by_xpath, p_add_xpath).text
    rt_p_add = p_add_text.split(':')
    return rt_p_add[1]

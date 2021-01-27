from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import datetime
import os
from dotenv import load_dotenv

# 前台开启浏览器模式
def openChrome():
    # 加启动配置
    option = webdriver.ChromeOptions()
    option.add_argument('disable-infobars')
    # 打开chrome浏览器
    # driver = webdriver.Chrome(chrome_options=option)
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver

# 登录
def operationAuth(driver):
    url = "https://move.muc.edu.cn/uc/wap/login?redirect=https%3A%2F%2Fmove.muc.edu.cn%2Fncov%2Fwap%2Fdefault%2Findex"
    driver.get(url)

    while driver.title != '中央民族大学—每日填报':
        # 输入账户与密码
        username = driver.find_element_by_xpath("//input[@placeholder='输入信息门户用户名']")
        password = driver.find_element_by_xpath("//input[@placeholder='输入信息门户密码']")
        username.send_keys(os.environ.get("username_env"))
        password.send_keys(os.environ.get("password_env"))

        # 提交登录申请
        driver.find_element_by_class_name('btn').click();
        time.sleep(5)

    wait = WebDriverWait(driver, 10)
    time.sleep(3)
    wait.until(EC.title_is('中央民族大学—每日填报'))
    print('登录完毕')
    print(datetime.datetime.now())
    
# 填表
def fillform(driver):
    
    # 填表
    driver.find_element_by_xpath("/html/body/div[1]/div/div/section/div[4]/ul/li[8]/div/input").click() # 填表a
    time.sleep(10) # 延时等待获取地理位置完毕
    print('填表完毕')
    print(datetime.datetime.now())
    
    # 提交
    driver.find_element_by_xpath("/html/body/div[1]/div/div/section/div[5]/div/a").click()
    time.sleep(5)
    driver.find_element_by_xpath("//*[@id='wapcf']/div/div[2]/div[2]").click() # confrim
    print('提交完毕')
    print(datetime.datetime.now())

    # close current page
    time.sleep(2)
    driver.close()

# 方法主入口
if __name__ == '__main__':
    load_dotenv()
    # 启动
    while True:
        driver = openChrome()
        operationAuth(driver)
        fillform(driver)
        time.sleep(86370)
#coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select  import Select
import selenium.webdriver.support.expected_conditions
import time


driver = webdriver.Firefox() # Get local session of firefox

#访问server网页
driver.get("http://118.194.49.143:8501/server/login?sessionTimeOut=true") # Load page

#判断是否进入了server的登录页
assert "博睿-Bonree Server".decode('utf8') in driver.title
#driver.title网页的标题<title>标签中的文字

#获取用户名
useName = driver.find_element_by_name("accountName") 
useName.send_keys("ldmtest")
#print useName.get_attribute("class")
#print useName.get_attribute("id")
#print useName.id 
#print useName.tag_name
#print useName.get_attribute("value")
#print useName.is_enabled()
#useName.screenshot('./name.png')  对元素截图


#获取密码
passwd = driver.find_element_by_name("password") 
passwd.send_keys("123456" )



#添加延时等待验证码出现
#time.sleep(2) 
driver.implicitly_wait(6)

#获取验证码
verifiCode = driver.find_element_by_name("validate_code") 
verifiCode.send_keys("bonree")

#print driver.current_url


assert selenium.webdriver.support.expected_conditions.element_to_be_clickable(driver) ,'元素可点击'
#登录
login = driver.find_element_by_xpath("//input[@class='login-btn']")
#login.send_keys(Keys.RETURN)   #键盘输入enter键
#鼠标点击
#ActionChains(driver).move_to_element(login).click(login).perform()
#ActionChains(driver).click(login).perform()
#ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
#ActionChains(driver).send_keys_to_element(login,Keys.ENTER).perform()
#ActionChains(driver).send_keys(Keys.ENTER).perform()
#ActionChains(driver).click(login).perform()
#login.click()
login.submit()
time.sleep(3)

#鼠标移到帐号名上
#account = driver.find_element_by_xpath("//span[@class='info hovershow floatShow']")
#ActionChains(driver).move_to_element(account).perform()
#time.sleep(3)


#print account.text  获取元素的text

#调用窗口管理器特定的“全屏”操作
#driver.fullscreen_window()
#time.sleep(3)

#t = driver.get_screenshot_as_base64()

#driver.get_screenshot_as_file('./test.png') 获得截图文件

#t = driver.get_screenshot_as_png()

#t = driver.get_window_position()  获取当期窗口位置

#t = driver.get_window_rect()

#print driver.name



#print driver.current_url
assert "ldmtest" in driver.page_source

#driver.execute_script("alert('nihao');") 页面执行js代码

#滚动页面 左右滚动
#driver.execute_script("window.scrollTo(50, 500);")
#driver.execute_script("window.scrollTo(arguments[0], 500);",50)
#driver.execute_script("window.scrollTo(arguments[0], arguments[1]);",50,500)
#移动到最下端
#driver.execute_script("window.scrollTo(50, document.body.scrollHeight);")

#拉到页面底部 上下滚动
#js = "var q=document.documentElement.scrollTop=10000"
#driver.execute_script(js)

#回到顶部
#js = "var q=document.documentElement.scrollTop=0"
#driver.execute_script(js)

#找到有数据的应用：
apms = driver.find_elements_by_xpath("//h4[@class='applicationname']")

t = None 
for apm in apms:
	if apm.text == "apmserver3.0_k  (别名:  apmserver3.0_k)":
		t = apm 

print t


time.sleep(5)






#关闭连接   
#driver.close() 关闭窗口
#关闭窗口和driver
driver.quit()   
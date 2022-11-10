from CouncilProcess import CouncilProcess

url = "https://ljubljana.kdmid.ru/queue/orderinfo.aspx?id=10756&cd=46df15aa&ems=1C0A409D"

process = CouncilProcess(url)
process.run()

# center_panel = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.ID, "center-panel"))
# filename = 'captcha_' + str(datetime.now().timestamp()).replace('.', '') + '.png'



# with open(filename, 'wb') as file:
#    l = driver.find_element(by=By.XPATH, value='//*[@alt="Необходимо включить загрузку картинок в браузере."]')
#    file.write(l.screenshot_as_png)

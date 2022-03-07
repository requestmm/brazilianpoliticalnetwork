
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import os

chromedriver_autoinstaller.install()



driver = webdriver.Chrome()
driver.get("https://divulgacandcontas.tse.jus.br/divulga/#/estados/2018/2022802018/BR/candidatos")


candidates_table = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[1]/div/div/section[3]/div/div/table[1]/tbody/tr[1]/td[1]/a"))
    )

candidates_links = driver.find_elements_by_css_selector("body > div.conteudo > div.container-fluid.dvg-main-wrap > div > div > section:nth-child(3) > div > div > table.table.table-hover.visible-md.visible-lg > tbody > tr td a")
candidates_links_length = len(candidates_links)

for n in range(1,candidates_links_length):
    driver.get("https://divulgacandcontas.tse.jus.br/divulga/#/estados/2018/2022802018/BR/candidatos")
    time.sleep(4)
    candidate_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.conteudo > div.container-fluid.dvg-main-wrap > div > div > section:nth-child(3) > div > div > table.table.table-hover.visible-md.visible-lg > tbody > tr:nth-child("+str(n)+") > td:nth-child(1) > a"))
    )
    candidate_link.click()
    time.sleep(4)
    statement_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/section[2]/div/div[1]/div[2]/button[2]"))
    )
    statement_link.click()
    time.sleep(4)
    export_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[1]/div/div/section[3]/div/div/div[1]/h3/span/a[1]"))
    )
    export_link.click()
    time.sleep(4)
    

driver.close()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os
import random
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from multiprocessing import Pool
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from faker import Faker
fake = Faker()
cwd = os.getcwd()

opts = Options()
opts.headless = False
opts.add_argument('log-level=3') 
dc = DesiredCapabilities.CHROME
dc['loggingPrefs'] = {'driver': 'OFF', 'server': 'OFF', 'browser': 'OFF'}
opts.add_argument('--ignore-ssl-errors=yes')
# opts.add_argument("--start-maximized")
# opts.add_argument("--start-fullscreen")
opts.add_argument('--ignore-certificate-errors')
opts.add_argument('--disable-blink-features=AutomationControlled')
opts.add_experimental_option('excludeSwitches', ['enable-logging'])
path_browser = f"{cwd}\chromedriver.exe"

#DATA USER
nama_user = "Ananda rizki budhi" 
kelas_ = "X mipa 4" #index nya adalah 6
kelas = 6
no_absen = 22

def open_browser(k):
    tanggal_pelaksanaan = k
    try:
        random_angka = random.randint(1,2)
        random_angka_satu = random.randint(100,999)
        random_angka_dua = random.randint(10,99)
        opts.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.{random_angka_satu}.{random_angka_dua} Safari/537.36")
        browser = webdriver.Chrome(options=opts, desired_capabilities=dc, executable_path=path_browser)
        browser.get('https://bit.ly/form_amalyaumi_bkpakizzul')
    
  
         

        nama = wait(browser,15).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
        
        nama.send_keys(nama_user) 
        sleep(0.5)
        
        tanggal =  wait(browser,15).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')))
        tanggal.send_keys(tanggal_pelaksanaan) 

        sleep(0.5)
        absen =  wait(browser,15).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')))
        absen.send_keys(no_absen) 

        sleep(0.5)
        #KELAS: /html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[1]/div[7]/span
        wait(browser,5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div"))).click()
        sleep(0.5)
        #KELAS XMIPA 1 = 3, X MIPA 2 = 4, X MIPA 3 = 5, XMIPA 4 = 6, XMIPA 5 = 7
        wait(browser,5).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[2]/div[{kelas}]'))).click()
        
        urutan = 2
        sleep(1)
        for check in range(0,5):
            wait(browser,5).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[{urutan}]/label[1]/div/div/div[2]"))).click()
            sleep(0.5)
            urutan = urutan + 2

        urutan = 2

        #click sholat sunnah
        for check in range(0,8):
            wait(browser,5).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[{urutan}]/label[{random_angka}]/div/div/div[2]"))).click()
            sleep(0.5)
            urutan = urutan + 2

        #Tilawah
        wait(browser,5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div[2]"))).click()
        sleep(0.5)
        wait(browser,5).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[2]/div[{random.randint(2,5)}]/span"))).click()
        sleep(0.5)
        wait(browser,5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div/span/span"))).click()

        sleep(1)
        try:
            get_text =  wait(browser,15).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[3]'))).text
            print(f"[*] {get_text}")
            with open('success.txt','a') as f:
                f.write('{0} | {1}\n'.format(nama_user,tanggal_pelaksanaan))
            browser.quit()
        except:
            print(f"[*] [  {tanggal_pelaksanaan} ] Automation Failed!")
            browser.quit()
    except:
        print(f"[*] [ {tanggal_pelaksanaan} ] Automation Failed!")
        browser.quit()
if __name__ == '__main__':
    global list_accountsplit
    print('[*] AAUTOMATION FILL GOOGLE FORM')
    print('[*] Author: RJD')
  
    file_list_akun = "tanggal.txt"
    myfile_akun = open(f"{cwd}/{file_list_akun}","r")
    akun = myfile_akun.read()
    list_accountsplit = akun.split()
    k = list_accountsplit
    
    for i in k:  
        open_browser(i)
    print('[*] AUTOMATION FINISH')    
        

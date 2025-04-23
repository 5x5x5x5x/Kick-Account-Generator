from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import string
import random

with open("6hanekombinasyon.txt", "r") as file:
    kodlar = [line.strip() for line in file if line.strip()]

random_gun = random.randint(1, 28)
random_ay = random.randint(1, 12)
random_yil = random.randint(1980, 2006)
tarih = f"{random_gun:02d}-{random_ay:02d}-{random_yil:04d}"

def generate_random_kadi():
    lenght = random.randint(6, 14)
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=lenght))

def generate_random_gmail():
    lenght = random.randint(7,15)
    letters_only = string.ascii_letters
    random_part = ''.join(random.choices(letters_only, k=lenght))
    return random_part.lower() + "@gmail.com"

kullaniciadi = generate_random_kadi()
gmail = generate_random_gmail()
sifre_str = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

def type_like_human(element, text, delay=0.1):
    element.click()
    for char in text:
        element.send_keys(char)
        sleep(delay)

print("Bu Proje Tüm Haklarıyla 5x5x5x5x (x)'e Aittir Bunu Parayla Aldıysanız Dolandırılmışsınız Demektir https://www.github.com/5x5x5x5x/Kick-Account-Generator")

driver = webdriver.Chrome()
driver.get("https://kick.com")
sleep(15)

driver.find_element(By.CSS_SELECTOR, '[data-test="sign-up"]').click()
sleep(2)

type_like_human(driver.find_element(By.NAME, "email"), gmail)
sleep(1)

date_input = driver.find_element(By.NAME, "birthdate")
date_input.clear()
date_input.send_keys(tarih)
sleep(1)

username_field = driver.find_element(By.NAME, "username")
current_username = kullaniciadi

while True:
    username_field.clear()
    type_like_human(username_field, current_username)
    sleep(1)
    try:
        driver.find_element(By.XPATH, "//p[contains(text(), 'Kullanıcı adı zaten alınmış')]")
        current_username += random.choice(string.ascii_lowercase + string.digits)
    except:
        break

type_like_human(driver.find_element(By.NAME, "password"), sifre_str)
sleep(1)

driver.find_element(By.XPATH, "//span[contains(text(), 'Kaydol')]").click()
sleep(3)

try:
    otp_input = driver.find_element(By.NAME, "code")
    for kod in kodlar:
        otp_input.clear()
        otp_input.send_keys(kod)
        otp_input.send_keys(Keys.ENTER)
        print(f"Denendi: {kod}")
        sleep(2)
        try:
            driver.find_element(By.CSS_SELECTOR, ".otp-error")
        except:
            print("✅ Hesap oluşturuldu!")
            with open("hesaplar.txt", "a", encoding="utf-8") as file:
                file.write(f"{gmail} | {sifre_str} | {current_username} | {tarih}\n")
            break
except Exception as e:
    print("OTP alanı bulunamadı ya da hata oluştu:", e)

sleep(10)
driver.quit()

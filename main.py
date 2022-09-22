from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time as ti
import smtplib
from email.mime.text import MIMEText


def email_2(message,v):
    sender = 'misterjakor@gmail.com'
    password = 'UliArtq8'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    try:
        server.login(sender, password)
        msg = MIMEText(message)
        server.sendmail(sender,v,msg.as_string())
    except Exception as _ex:
        return f"{_ex}\nCheck your login or password please!"

def email_(message,v):
    sender = 'misterjakor@gmail.com'
    password = 'UliArtq8'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg["Subject"] = "инфа"
        server.sendmail(sender,v,msg.as_string())
    except Exception as _ex:
        return f"{_ex}\nCheck your login or password please!"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://pr-cy.ru/roskomnadzor")
f=input("дай домЭн:")
g = driver.find_element_by_css_selector("input")
g.send_keys(f)
g1=driver.find_element_by_css_selector("button").click()
ti.sleep(5)
k="fsfre"
f2=k
try:
    k = driver.find_element_by_css_selector(".prcy-ektqja div.prcy-y8qa8s")
    f2 = k.text
except:
    rtt="ggg"
k2 = driver.find_element_by_class_name("prcy-1jzs7ec")
r=k2.text
r=r.replace("Доступные лимиты: ","")
r=r.replace(" из 300","")
r=int(r)
o=True
while f2=="IP адрес и домен не найден в реестре." and r!=0:
    ti.sleep(60)
    g1 = driver.find_element_by_css_selector("button").click()
    k = driver.find_element_by_css_selector(".prcy-ektqja div.prcy-y8qa8s")
    k2 = driver.find_element_by_class_name("prcy-1jzs7ec")
    r = k2.text
    r = r.replace("Доступные лимиты: ", "")
    r = r.replace(" из 300", "")
    r = int(r)
    f2 = k.text
    if r==0:
        o=False
v="leha.tkachov@gmail.com"
message="Петухи заблокировали домен"
m="усе"
if o==False and f2=="IP адрес и домен не найден в реестре.":
    email_2(m,v)
if o==True:
    email_(message, v)
if o==False and f2!="IP адрес и домен не найден в реестре.":
    email_(message,v)
driver.close()
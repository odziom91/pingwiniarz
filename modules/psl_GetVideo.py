from urllib import request
from bs4 import BeautifulSoup

def GetNvidia_nfb():
    page = request.urlopen("https://www.nvidia.pl/Download/processFind.aspx?psid=101&pfid=817&osid=12&lid=14&whql=5&lang=pl&ctk=0&qnfslb=01")
    soup = BeautifulSoup(page, features="html.parser")
    driver_list = soup.findAll('tr', attrs={'id' : 'driverList'})
    soup_driver = BeautifulSoup(str(driver_list[0]), features="html.parser")
    driver = soup_driver.findAll('td', attrs={'class' : 'gridItem'})
    driver_name = driver[1].text
    driver_version = driver[2].text
    driver_date = driver[3].text
    return driver_name, driver_version, driver_date

def GetNvidia_pb():
    page = request.urlopen("https://www.nvidia.pl/Download/processFind.aspx?psid=101&pfid=817&osid=12&lid=14&whql=1&lang=pl&ctk=0&qnfslb=01")
    soup = BeautifulSoup(page, features="html.parser")
    driver_list = soup.findAll('tr', attrs={'id' : 'driverList'})
    soup_driver = BeautifulSoup(str(driver_list[0]), features="html.parser")
    driver = soup_driver.findAll('td', attrs={'class' : 'gridItem'})
    driver_name = driver[1].text
    driver_version = driver[2].text
    driver_date = driver[3].text
    return driver_name, driver_version, driver_date

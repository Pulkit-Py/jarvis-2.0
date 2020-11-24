from speech import take
from wish import wishme
from speek import sp
from chatbot import chatty
import  wikipedia
import webbrowser
import os
import random
import datetime
from bs4 import BeautifulSoup  as soup
from urllib.request import urlopen
import smtplib
import socket 
import subprocess 
import texttable as tt
import requests
import pandas as pd 
from nsetools import Nse 
import platform
import phonenumbers 
from phonenumbers import geocoder , carrier 


f = open("password.txt", "r")
password = f.read()

pulkit = {
    "name" : "Enter your name ",
    "email" : "Enter your mail here",
}

def zodiac_sign(day, month): 
    if month == 'december': 
        astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'          
    elif month == 'january': 
        astro_sign = 'Capricorn' if (day < 20) else 'aquarius'          
    elif month == 'february': 
        astro_sign = 'Aquarius' if (day < 19) else 'pisces'          
    elif month == 'march': 
        astro_sign = 'Pisces' if (day < 21) else 'aries'         
    elif month == 'april': 
        astro_sign = 'Aries' if (day < 20) else 'taurus'       
    elif month == 'may': 
        astro_sign = 'Taurus' if (day < 21) else 'gemini'     
    elif month == 'june': 
        astro_sign = 'Gemini' if (day < 21) else 'cancer'      
    elif month == 'july': 
        astro_sign = 'Cancer' if (day < 23) else 'leo'    
    elif month == 'august': 
        astro_sign = 'Leo' if (day < 23) else 'virgo'     
    elif month == 'september': 
        astro_sign = 'Virgo' if (day < 23) else 'libra'     
    elif month == 'october': 
        astro_sign = 'Libra' if (day < 23) else 'scorpio'     
    elif month == 'november': 
        astro_sign = 'scorpio' if (day < 22) else 'sagittarius'     
    print("jarvis:"+astro_sign) 
    sp(astro_sign)

def getdata(url): 
    r = requests.get(url) 
    return r.text 

def main():
    wishme()
    while(True):
        query = take().lower()
        if "None" not in query:
            value = chatty(query)
            if value is not None:
                print("jarvis : "+ value)
                sp(value)
            else:
                if "search" in query:
                    try:
                        sp("searching....")
                        result = wikipedia.summary(query,sentences=1)
                        print("Jarvis: "+result)
                        sp(result)
                    except Exception :
                        sp("soory i didn't find anything try again")

                elif "open" in query:
                    chrome_path =" C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                    query = query.replace("open","")
                    res = query.split()
                    for i in res:
                        if ".com" in i:
                            sp("sure sir")
                            webbrowser.get(chrome_path).open(i)

                elif "calculate" in query:
                    query = query.replace("into","*")
                    query = query.replace("multiply","*")
                    query = query.replace("divide","/")
                    query = query.replace("by","/")
                    res = query.split()
                    temp = []
                    for i in res:
                        if i.isdigit() or '+'in i or "*" in i or '-' in i or '/' in i:
                            temp.append(i)
                    answer = ''.join(temp) 
                    ans = eval(answer)
                    print("jarvis: the answer is "+ str(ans))
                    sp("the answe is "+ str(ans))

                elif 'play music' in query:
                    music_dir = "F:\\Playlist"
                    songs = os.listdir(music_dir)
                    song = random.choice(songs)
                    os.startfile(os.path.join(music_dir,song))

                elif "the time" in query:
                    time = datetime.datetime.now().strftime("%H:%m:%S")
                    print("jarvis: the time is "+ str(time))
                    sp("sir the time is "+ str(time))

                elif "want to say something" in query:
                    print("jarvis: please like the video subsribe Pulkit py.")
                    sp("please like the video and subsribe Pulkit py")

                elif "latest news" in query:
                    root = urlopen("https://news.google.com/news/rss")
                    xmlpage = root.read()
                    root.close()
                    page = soup(xmlpage,'xml')
                    news = page.findAll("item")
                    stop = 1
                    for new in news:
                        print("jarvis:"+new.title.text)
                        sp(new.title.text)
                        print(new.pubDate.text)
                        print('-'*60)
                        print('\n')
                        if stop == 2:
                            break
                        stop = stop + 1

                elif "send mail" in query:
                    s = smtplib.SMTP('smtp.gmail.com',587)
                    s.starttls()
                    s.login(pulkit["email"],password)
                    sp("Please type the email-id")
                    reciver_emai = input("Email-id :")
                    sp("Please type the Message ")
                    message = input("send message :")
                    s.sendmail(pulkit["email"],reciver_emai,message)
                    s.quit()
                    print("Jarvish: email Send to"+reciver_emai)
                    sp("email Send to"+reciver_emai)

                elif "astro sign" in query:
                    sp("Please enter the Date you born")
                    day = int(input("day "))
                    sp("Please enter the month you born")
                    month = input("month ")
                    zodiac_sign(day, month) 

                elif "get my ip" in query:
                    try: 
                        host_name = socket.gethostname() 
                        host_ip = socket.gethostbyname(host_name)
                        print("Hostname :  ",host_name) 
                        print("IP : ",host_ip) 
                        sp("Hostname :  "+host_name)
                        sp("IP : "+host_ip) 
                    except: 
                        print("Unable to get Hostname and IP") 

                elif "available wi-fi" in query:
                    devices = subprocess.check_output(['netsh','wlan','show','network']) 
                    devices = devices.decode('ascii') 
                    devices = devices.replace("\r","") 
                    sp("Here is the result.")
                    print(devices)

                elif "covid case" in query:
                    url = 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'
                    page = requests.get(url) 
                    case = soup(page.text, 'html.parser') 
                    data = [] 
                    data_iterator = iter(case.find_all('td'))  
                    while True: 
                        try: 
                            country = next(data_iterator).text 
                            confirmed = next(data_iterator).text 
                            deaths = next(data_iterator).text 
                            continent = next(data_iterator).text  
                            data.append(( 
                                country, 
                                confirmed.replace(', ', ''), 
                                deaths.replace(', ', ''), 
                                continent 
                            )) 
                        except StopIteration: 
                            break
                    data.sort(key = lambda row: row[1], reverse = True)
                    table = tt.Texttable() 
                    table.add_rows([(None, None, None, None)] + data) 
                    table.set_cols_align(('c', 'c', 'c', 'c'))
                    table.header((' Country ', ' Number of cases ', ' Deaths ', ' Continent ')) 
                    sp("Data is here")
                    print(table.draw()) 

                elif "covid vaccine" in query:
                    r = requests.get("https://covid-19tracker.milkeninstitute.org/")  
                    htmldata = r.text 
                    data = soup(htmldata, 'html.parser') 
                    result = str(data.find_all("div", class_="is_h5-2 is_developer w-richtext")) 
                    sp("Top 5 results are")
                    print("NO 1 " + result[46:86]) 
                    print("NO 2 "+result[139:226]) 
                    print("NO 3 "+result[279:305]) 
                    print("NO 4 "+result[358:375]) 
                    print("NO 5 "+result[428:509]) 

                elif "show fuel price" in query:
                    htmldata = getdata("https://www.goodreturns.in/petrol-price.html") 
                    data = soup(htmldata, 'html.parser') 
                    mydatastr = '' 
                    result = [] 
                    for table in data.find_all('tr'): 
                        mydatastr += table.get_text() 
                    mydatastr = mydatastr[1:] 
                    itemlist = mydatastr.split("\n\n") 
                    for item in itemlist[:-5]: 
                        result.append(item.split("\n")) 
                    df = pd.DataFrame(result[:-8]) 
                    sp("Here is the result.")
                    print(df) 

                elif "stock price" in query:
                    nse = Nse() 
                    sp("please enter company symbol")
                    code = input("company symbol ")
                    quote = nse.get_quote(code) 
                    value = quote['averagePrice'] 
                    print("Average Price  : " + str(value))
                    sp("Average Price " + str(value)) 
                
                elif "play youtube song" in query:
                    url = 'https://www.youtube.com/watch?v=gTZOLaaQihs&t=579s'
                    chrome_path =" C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                    sp("Playing youtube video")
                    webbrowser.get(chrome_path).open(url)

                elif "computer details" in query:
                    my_system = platform.uname()
                    sp("System information is here ")
                    print(f"System: {my_system.system}")
                    print(f"Node Name: {my_system.node}")
                    print(f"Release: {my_system.release}")
                    print(f"Version: {my_system.version}")
                    print(f"Machine: {my_system.machine}")
                    print(f"Processor: {my_system.processor}")

                elif "phone number" in query:
                    sp("Plese type mobile number")
                    phone_number = phonenumbers.parse(input("Number with country code : "))  
                    country = geocoder.description_for_number(phone_number,'en')
                    provider = carrier.name_for_number(phone_number,'en')
                    print(country) 
                    print(provider)   
                    sp("This Number belong to "+country+"And the provider is" + provider)

                elif "system information" in query:
                    data = subprocess.check_output(['ipconfig','/all']).decode('utf-8').split('\n') 
                    sp("System information is here ")
                    for item in data: 
                        print(item.split('\r')[:-1])
                elif "job for me" in query:
                    res = '' 
                    htmldata = getdata("https://www.sarkariresult.com/latestjob.php") 
                    result = soup(htmldata, 'html.parser') 
                    for li in result.find_all("div", id="post"): 
                        res += (li.get_text()) 
                    print(res) 
                    sp("Check all the job")

                elif "stop" in query:
                    sp("bye bye sir")
                    break
        else:
            sp("can you speek again ")
main()

        
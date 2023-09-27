#!/usr/bin/env python3

# Script Name:               Cookie Monster
# Author:                    Gerald
# Date of latest revision:   8/29/2023
# Purpose:                   cookie 

# Sources:
# - https://pypi.org/project/requests/ 
# - https://requests.readthedocs.io/en/latest/user/quickstart/#cookies 

# The below Python script shows one possible method to return the cookie from a site that supports cookies.
import requests
from bs4 import BeautifulSoup
import webbrowser

# targetsite = input("Enter target site:") # Uncomment this to accept user input target site
targetsite = "http://www.whatarecookies.com/cookietest.asp" # Comment this out if you're using the line above
response = requests.get(targetsite)
cookie = response.cookies

def bringforthcookiemonster(): # Because why not!
    print('''

              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.

        ''')

bringforthcookiemonster()
print("Target site is " + targetsite)
print(cookie)

# Add here some code to make this script perform the following:
# - Send the cookie back to the site and receive a HTTP response
def sendcookie():
    r = requests.get(targetsite, cookies=cookie)
    r.text 
# - Generate a .html file to capture the contents of the HTTP response
#- Open it with Firefox

def html_file():
  #user input variable 
  url = input("input a URL: ")
  # sends a http get request to the url variable and saves that as a variable
  response = requests.get(url)
  # if we get a successful request (200 is the response code for a successful request) then...
  if response.status_code == 200:
    # parses the html and saves it as a variable
      soup = BeautifulSoup(response.text, 'html.parser')
    # with the captured response html open, write in encoding utf 8 as a html file, and write it as a string
      with open('captured_response.html', 'w', encoding='utf-8') as html_file:
          html_file.write(str(soup))
        # open captured response in a new tab
      webbrowser.open('captured_response.html', new=2)
  else:
      print("an error has occured")




#
# Stretch Goal
# - Give Cookie Monster hands
#!/usr/bin/env python3

# Author:      Abdou Rockikz
# Description: XSS detection  
# Date:        9/26/2023
# Modified by: Gerald Reitmeyer

# Import libraries

import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

# Declare functions

### makes a funciton called get_all to goes to a url, gets all the forms and returns them
def get_all_forms(url):
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")

# function that gets the actions methods and inputs of a url and html forms and stores it
def get_form_details(form):
    # makes a function called get form details, makes a variable called details as an empty dictionary
    details = {}
    # makes a variable called action 
    action = form.attrs.get("action").lower()
    # makes a variable called method 
    method = form.attrs.get("method", "get").lower()
    # makes a variable called inputs as an empty list
    inputs = []
    # for each input tag in the form, get the input types and add them to the empty list of inputs
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    # adds action, method, and inputs to their respective empty list
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    # returns the details empty dictionary 
    return details

# Function that looks at a url and HTML forms then sends it as a get or post request
# makes a function called submit_form with the attributes form_details, url, value
# makes a variable called target_url that combines two urls(?)
# makes a variable called inputs that checks the type of inputs the HTML forms allow? I had to ask ChatGPT for this one
# makes a variable called data that starts off as a empty dictionary 
# then for each input in inputs...
    # if the input type is text or search then assign those input types to value
    # stores input_name as a variable
    # stores input_value as a variable
    # if there is input name and value then its put into the empty data variable
# if the form details include post...
    # puts the post form data into the data variable 
    # everything else will use http get sent to the url with the data variable used as a parameter. Chat GPT also helped with this one, I genuinely had zero idea what this meant
def submit_form(form_details, url, value):
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            data[input_name] = input_value

    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)

# Java script function that sees if the website accepts java script as a input and sets a alarm pop up if it does
# this function gets all HTML forms from a provided url, then prints the detected forms on that URL. 
# A variable called js_script that stores java script code that can be executed if the web application has XSS vulnerability
# makes and sets is_vulnerable variable to false
# then for each form in the forms variable do...
   #gets the form details 
   #pulls form details from the url, and pulls down the java script
   #then if there is java script in those forms...
        # prints XSS detected on provided URL
        # prints form details
        # sets is_vulnerable to true
# then at the end returns wheter the is_vulnerable variable is true or false
def scan_xss(url):
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    #js_script = ### TODO: Add HTTP and JS code here that will cause a XSS-vulnerable field to create an alert prompt with some text. 
    js_script = <script>alert(vulnerability detected)</script>
    is_vulnerable = False
    for form in forms:
        form_details = get_form_details(form)
        content = submit_form(form_details, url, js_script).content.decode()
        if js_script in content:
            print(f"[+] XSS Detected on {url}")
            print(f"[*] Form details:")
            print(form_details)
            is_vulnerable = True
    return is_vulnerable

# Main


if __name__ == "__main__":
    url = input("Enter a URL to test for XSS:") 
    print(scan_xss(url))

### TODO: When you have finished annotating this script with your own comments, copy it to Web Security Dojo
### TODO: Test this script against one XSS-positive target and one XSS-negative target
### TODO: Paste the outputs here as comments in this script, clearling indicating which is positive detection and negative detection

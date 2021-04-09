# -*- coding: utf-8 -*-
import time
import requests
from flask import Flask, redirect, url_for, request
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
app = Flask(__name__)


@app.route('/')
@app.route('/post')
# def hello_world():
#     r=requests.get('https://www.enforta.ru/contacts/branches/cherepovec.html', verify=False)
#     ht=r.content
#     print(ht)
#
#     # close web browser
#     r.close()
#     return ht

@app.route('/get',methods = ['POST', 'GET'])
def return_html():
    if request.method == 'POST':
        arges = dict(request.form.deepcopy())

        try:
            print (arges)
            print(request.args)
            if arges.get("proxyUrl"):
                url= arges.get("proxyUrl")
                arges.pop("proxyUrl")
                r = requests.post(url=url, data=arges, verify=False)
                ht = r.content
                # close web browser
                r.close()
                return ht
            else:
                return "Неудачные параметры"
        except:
            return "Неудачные параметры"

    else:
        try:
            arges = dict(request.args.deepcopy())
            print(arges)
            if arges.get("proxyUrl"):
                url= arges.get("proxyUrl")
                arges.pop("proxyUrl")
                r = requests.get(url=url, params=arges, verify=False)
                ht = r.content

                # close web browser
                r.close()
                return ht
            else:
                return "Неудачные параметры"
        except:
            return "Неудачные параметры"

if __name__ == '__main__':
    app.run()

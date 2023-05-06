# -*- coding: utf-8 -*-

import datetime
from flask import Flask, redirect, url_for, request
app = Flask(__name__)


@app.route('/')
@app.route('/post')
@app.route('/get',methods = ['POST', 'GET'])
def return_html():
        arges = dict(request.form.deepcopy())

        try:
            print (arges)
            print(request.args)
            print (request.data)
            with open('logger.txt','r', encoding='UTF-8') as fi:
                cc=fi.read()

            with open('logger.txt','w', encoding='UTF-8') as fi:
                poster=f'''{datetime.datetime.now()}
                { ', '.join( [f'{k}:{dict(arges)[k]}' for k in dict(arges)]) }
                { ', '.join( [f'{k}:{dict(request.args)[k]}' for k in dict(request.args)]) }
                {request.data}
                {'----------------------------------------------'}
                
                '''
                fi.write(poster+cc)
            return poster.replace('\n','<br/>')
        except Exception as e:
            return str(e)
            return "Неудачные параметры"

@app.route('/show',methods = ['GET'])
def return_req():

    try:
        with open('logger.txt','r', encoding='UTF-8') as fi:
            return str(fi.read().replace('\n','<br/>'))
    except Exception as e:
        return str(e)
        return "Неудачные параметры"



if __name__ == '__main__':
    app.run()

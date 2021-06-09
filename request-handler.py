from ReMark.remark import compile
import flask
from flask import request
import sqlite3

connection = sqlite3.connect('remark-api.db')
cursor = connection.cursor()

""" 
Private License (Copyright Shaun Cameron)
author/s: Shaun Cameron, Gary Kong ( In spirit )
creation: 08/06/2021 - 08/06/2021
requires: Flask, ReMark [ Regex ], remark [ ReMark, yaml ]
"""

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def openread(file):

    return open(file, 'r').read()

def authAPIID():

    if 'key' in request.args:

        """ check auth id """

        if request.args['key'] == '0x1019-1093-5738-1092-1825':

            return True

        else:

            return '<p style="color:red;"> API call made with <b> invalid key </b> header </p>'

    else:

        return '<p style="color:red;"> API call made without <b> key </b> header </p>'

@app.route('/api/remark/', methods=['GET'])
def api_remark():

    result = authAPIID()

    if result == True:

        if 'string' in request.args:

            compilation = compile(request.args['string'], None, True)

            if 'wrap' in request.args and request.args['wrap'] == 'true':

                return compilation

            else:

                return '<div class="remark-field">' + compilation + '</div>'

        else:

            return compile(openread('rmk/errors/nostringheader.rmk'), None, False)

    else:

        return result

app.run()
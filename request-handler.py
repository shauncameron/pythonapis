from ReMark.remark import compile
from Egg import createID, Egg
import flask
from flask import request

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

        if request.args['key'] in open('api.keys', 'r').read().split('\n'):

            return True

        else:

            return '<p style="color:red;"> API call made with <b>invalid key</b> header </p>'

    else:

        return '<p style="color:red;"> API call made without <b>key</b> header </p>'


@app.route('/api/remark/', methods=['GET'])
def api_remark():
    result = authAPIID()

    if result == True:

        if 'string' in request.args:

            try:

                compilation = compile(request.args['string'], None, True)

                if 'wrap' in request.args and request.args['wrap'] == 'true':
                    return compilation

            except:

                return '<p style="color:red;">Python Exception</p>'

            else:

                return '<div class="remark-field">' + compilation + '</div>'

        else:

            return compile(openread('rmk/errors/nostringheader.rmk'), None, False)

    else:

        return result


# Scrambling

@app.route('/api/egg', methods=['GET'])
def api_eggs():
    result = authAPIID()

    if result == True:

        if 'createuid' in request.args:

            try:

                return createID()

            except Exception as e:

                return '<p style="color:red;">Python Exception', e, '</p>'

        elif 'encrypt' in request.args:

            if 'with' in request.args:

                try:

                    return Egg(request.args['with']).decrypt(request.args['encrypt'])

                except Exception as e:

                    return '<p style="color:red;">Python Exception', e, '</p>'

            else:

                return '<p style="color:red;">Missing "with" header argument</p>'

        elif 'decrypt' in request.args:

            if 'with' in request.args:

                try:

                    return Egg(request.args['with']).decrypt(request.args['decrypt'])

                except Exception as e:

                    return '<p style="color:red;">Python Exception', e, '</p>'

            else:

                return '<p style="color:red;">Missing "with" header argument</p>'

        else:

            return '<p style="color:red;">Call to egg but not specifying (encrypt|decrypt|creatuid)</p>'

    else:

        return result


@app.route('/', methods=['GET'])
def index():
    return '<p style="color:red;"><b> index not valid </b></p>'


@app.route('/api', methods=['GET'])
def api():

    return '<p style="color:red;"><b> base api not valid </b></p>'


# Start server default http/s port -> 80

from socket import gethostname, gethostbyname

app.run(host=gethostbyname(gethostname()), port=80)

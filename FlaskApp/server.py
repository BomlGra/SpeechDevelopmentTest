#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from flask import render_template
import config
import os
import uuid

import random
import logging

import grpc
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

import ui_pb2
import ui_pb2_grpc


app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        # audio_bytes = request.files['audio_data'].read()
        # audio_files = ...
        uploaded_files = request.files.getlist("records[]")
        audio_files = list(map(lambda f: ui_pb2.Audio(content=f.read()), uploaded_files))
        # print(audio_files)
        print(len(audio_files))
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = ui_pb2_grpc.NNetworkStub(channel)        
            result = stub.GetScore(ui_pb2.Audios(audios=audio_files))
            print(result.message)
            print('files uploaded successfully')

        return render_template('index.html', request="POST")
    else:
        return render_template("index.html")

@app.route("/account")
def account():
    return render_template('account.html')
@app.route("/moreAbout")
def moreAbout():
    return render_template('moreAbout.html')
@app.route("/test")
def test():
    return render_template('test.html')


@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')
@app.route('/signUp',methods=['POST'])
def signUp():
 
    # read the posted values from the UI
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']
 
    # validate the received values
    if _name and _email and _password:
        return json.dumps({'html':'<span>All fields good !!</span>'})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})



if __name__ == "__main__":
    app.run(debug=True)
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


from SpeechDevelopmentTest.protos.storage import storage_pb2_grpc
from SpeechDevelopmentTest.protos.storage import storage_pb2
from google.protobuf.empty_pb2 import Empty

if __name__ == "__main__":
    channel = grpc.insecure_channel('localhost:50051')
    stub = storage_pb2_grpc.StorageStub(channel)
    # response = stub.GetQuestions(Empty())
    # for q in response.questions:
    #     print(q)
    # resp = stub.StartAttempt(storage_pb2.StartAttemptRequest(
    #         user_id=1,
    #     ),
    # )
    # print(resp.attempt_id)
    # stub.AttachReportToAttempt(storage_pb2.AttachReportToAttemptRequest(
    #     attempt_id=3,
    #     report=storage_pb2.Report(
    #         phonetic_score=3,
    #         grammar_score=5,
    #         vocabular_score=2,
    #         coherent_speech_score=4,
    #     )
    # ))
    # resp = stub.GetReportByAttempt(storage_pb2.GetReportByAttemptRequest(attempt_id=3))
    # print(resp.report)
    # print(resp.report.created_at.nanos)
    # f = open('/Users/alpha/Projects/Students/shumak/SpeechDevelopmentTest/Untitled.wav', 'rb')
    # byt = f.read()
    # stub.UploadAudio(storage_pb2.UploadAudioRequest(
    #     audio=storage_pb2.Audio(
    #         attempt_id=3,
    #         question_id=1,
    #         content=byt,
    #     )
    # ))
    resp = stub.GetAudiousInArchive(storage_pb2.GetAudiousInArchiveRequest(
        attempt_id=3,
    ))
    channel.close()
    with open('attempt_3.zip', 'wb') as f:
        f.write(resp.archive)
    app.run(debug=True)
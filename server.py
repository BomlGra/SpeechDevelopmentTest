#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from flask import render_template
import os

import random
import logging

import grpc
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

import recognizer_pb2
import recognizer_pb2_grpc


app = Flask(__name__)

def gener(audio_bytes):
    # audio_bytes = None
    # with open('test.wav', 'rb') as audio_file:
    #     audio_bytes = audio_file.read()
    yield recognizer_pb2.Chunk(Content=audio_bytes)


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        f = request.files['audio_data'].read()
        print('file uploaded successfully')
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = recognizer_pb2_grpc.NNetworkStub(channel)        
            result = stub.GetAudio(gener(f))
            print(result.message)
            # with open('audio.wav', 'wb') as audio:
            #     f.save(audio)

        return render_template('index.html', request="POST")
    else:
        return render_template("index.html")


if __name__ == "__main__":
    context = ('web.crt', 'web.key')
    app.run(host='0.0.0.0', port=5000, debug=True, ssl_context=context)
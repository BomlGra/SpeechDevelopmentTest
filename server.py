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

import recognizer_pb2
import recognizer_pb2_grpc
from models.audio import Audio
user_id = 6


app = Flask(__name__)

def gener(audio_bytes):
    yield recognizer_pb2.Chunk(Content=audio_bytes)

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        audio_bytes = request.files['audio_data'].read()
        
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = recognizer_pb2_grpc.NNetworkStub(channel)        
            result = stub.GetAudio(gener(audio_bytes))
            print(result.message)
            saved_path = config.AUDIO_DIR + str(uuid.uuid4()) + '.mp3'
            f = open(saved_path, 'wb')
            f.write(audio_bytes)
            f.close()

            Audio.create(
                path=saved_path,
                user=user_id,
            )
            print('file uploaded successfully')

        return render_template('index.html', request="POST")
    else:
        return render_template("index.html")


if __name__ == "__main__":
    context = ('web.crt', 'web.key')
    app.run(host='0.0.0.0', port=5000, debug=True, ssl_context=context)
from flask import Flask, render_template, json, request
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

# @app.route("/test", methods=['POST', 'GET'])
# def test():
#     if request.method == "POST":
#         audio_bytes = request.files['audio_data'].read()
        
#         with grpc.insecure_channel('localhost:50051') as channel:
#             stub = recognizer_pb2_grpc.NNetworkStub(channel)        
#             result = stub.GetAudio(gener(audio_bytes))
#             print(result.message)
#             saved_path = config.AUDIO_DIR + str(uuid.uuid4()) + '.mp3'
#             f = open(saved_path, 'wb')
#             f.write(audio_bytes)
#             f.close()

#             Audio.create(
#                 path=saved_path,
#                 user=user_id,
#             )
#             print('file uploaded successfully')

#         return render_template('test.html', request="POST")
#     else:
#         return render_template("test.html")


@app.route("/signup", methods=['POST', 'GET'])
def sign_up():
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
            print('auth data uploaded successfully')

        return render_template('signup.html', request="POST")
    else:
        return render_template("signup.html")


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


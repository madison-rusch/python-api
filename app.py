from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/info", methods=["GET"])
def info():
    return "Hello, World!"

# @app.route('/my-first-api', methods = ['GET'])
# def hello():
#     name = request.args.get('name')
#     if name is None:
#         text = 'Hello!'
#     else:
#         text = 'Hello ' + name + '!'
#     return text

@app.route("/get-iris")
def get_iris():

    import pandas as pd
    url ='https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv'
    iris = pd.read_csv(url)

    return jsonify({
        "message": "Iris Dataset",
        "data": iris.to_dict()
        })
    
@app.route("/say-hello")
def say_hello():
    return "Hello, World!"
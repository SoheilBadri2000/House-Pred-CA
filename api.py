from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

@app.route("/post_CA", methods=["POST"])
def post_CA():
    data = request.get_json()
    print(f"\n\nReceived data:\n {data}\n\n")
    print(pd.json_normalize(data).info())
    # Process the data and return a response if needed
    return "1000000"
    # return jsonify(data)

if __name__ == "__main__":
    app.run(port=5000)

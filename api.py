from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

@app.route("/post_CA", methods=["POST"])
def post_CA():
    data = request.get_json()
    print(f"\n\nReceived dat:\n {data}\n\n")
    print(pd.json_normalize(data))
    # Process the data and return a response if needed
    return "server received your data"
    # return jsonify(data)

if __name__ == "__main__":
    app.run(port=5000)

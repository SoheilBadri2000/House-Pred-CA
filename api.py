from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/post_CA", methods=["POST"])
def post_CA():
    data = request.get_json()
    print(f"Received data\n: {data}")
    # Process the data and return a response if needed
    return jsonify(data)

if __name__ == "__main__":
    app.run(port=5000)

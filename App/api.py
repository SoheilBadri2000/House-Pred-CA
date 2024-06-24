from flask import Flask, request, jsonify
from flask_cors import CORS
from app import process_ON

app = Flask(__name__)
CORS(app)

@app.route("/post_CA", methods=["POST"])
def post_CA():
    data = request.get_json()
    print(f"\n\nReceived data:\n {data}\n\n")
    
    # Process the data and return a response if needed
    # return "1000000"
    res = int(process_ON(data))
    print(f"\n\n{res}\n\n")
    return str(res)
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

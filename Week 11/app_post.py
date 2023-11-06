from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/post_json', methods=['POST'])
def post_json_data():
    post_data = request.get_json()
    return post_data

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)


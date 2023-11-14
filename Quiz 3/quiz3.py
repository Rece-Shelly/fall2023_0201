from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/whoareyou/<parameter>')
def whoareyou(parameter):
    response_data = {
        'name': 'Kamil',
        'email': 'kaa108@pitt.edu',
        'Python experience': 5,
        'Flask cool': True,
        'Parameter': parameter
    }

    return jsonify(response_data)  # or you could use json.dumps but for Flask applications we should use jsonify


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9500, debug=True)


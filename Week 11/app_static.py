from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/hello_static")
def hello_world_static():
    return render_template('static_hello.html')

@app.route("/hello_template")
def hello_world_template():
    return render_template('hello.html', hello_message ='Hello, World! from template')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)


from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hello_control_flow")
def hello_world_template():
    return render_template('control_flow.html', 
                           hello_message ='Hello, World! from template',
                           number_message = 15)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)


from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
    return "<p>Sample</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

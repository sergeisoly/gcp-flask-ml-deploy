from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    print("I am inside hello world")
    return 'Hello World! CD'

@app.route('/echo/<name>')
def echo(name):
    print(f"This was placed in the url: new-{name}")
    val = {"new-name": name}
    return jsonify(val)

@app.route('/who-is-the-best-ml-engineer')
def best():
    """Return the best ml engineer name"""
    print("printing some stuff")
    return '\"Nikita Radchenko is the best ML engineer. No doubts.\" - Sergei Solovev'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

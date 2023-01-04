from flask import Flask
from os import environ

app = Flask(__name__)

@app.route("/")
def main():
    if environ.get('Foo') is not None:
        str = "Exist var 'Foo' with value:" + environ.get('Foo')
        return str
    else: 
        return "Var 'Foo' not exist"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

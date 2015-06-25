from flask import Flask
app = Flask(__name__)


@app.route("/")
def say_hi():
    return "Hello world!"


@app.route("/hello/<name>")
def hi_person(name):
    return "Hello {}!".format(name.title())
    
@app.route("/hello/<name>")
def hi_person(name):
    return "Hello {}!".format(name.title())

if __name__ == '__main__':
    app.run()

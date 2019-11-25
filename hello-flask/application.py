from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/names")
def names():
    import random
    names = ['Matthew','Luke','Thomas','Peter','John','Mark']
    return "Your random name is: %s" % random.choice(names)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
from flask import Flask
app = Flask(__name__)

@app.route('/<user_name>')
def hello_name(user_name):
    return "Welcome {}!".format(user_name)

@app.route("/")
def hello():
  return "Hello World!"

if __name__ == "__main__":
  app.run()